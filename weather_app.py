import urllib.request   
import json 
import os
import requests
from datetime import datetime

API_KEY = os.environ.get("WEATHER_API_KEY")  
if not API_KEY:
    print("API key not found. Create a .env file with WEATHER_API_KEY=your_key")
    exit()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather" 
from urllib.parse import quote



HISTORY_FILE = "weather_history.json"

def save_to_history(city, data):
    """Append one lookup to weather_history.json."""
    if not data:
        return

    record = {
        "city": city,
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except (json.JSONDecodeError, OSError):
            history = []   # corrupt or unreadable file → start fresh

    history.append(record)

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)



def show_history():
    """Print all past lookups from weather_history.json."""
    if not os.path.exists(HISTORY_FILE):
        print("No history yet — look up a city first.")
        return

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Could not read history file.")
        return

    if not history:
        print("📭 History is empty.")
        return

    print(f"\nHistory ({len(history)} lookups):\n")
    print(f"{'When':<18} {'City':<18} {'Temp':>8} {'Weather':<25}")
    print("-" * 72)

    for rec in history:
        print(
            f"{rec.get('timestamp', '?'):<18} "
            f"{rec.get('city', '?'):<18} "
            f"{rec.get('temp', 0):>6.1f}°  "
            f"{rec.get('description', '?'):<25}"
        )
    print()







FAVOURITES_FILE = "favourites.json"

def load_favourites():
    """Return the saved favourites list, or [] if none."""
    if not os.path.exists(FAVOURITES_FILE):
        return []
    try:
        with open(FAVOURITES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []

def save_favourites(favourites):
    """Write the favourites list to disk."""
    with open(FAVOURITES_FILE, "w", encoding="utf-8") as f:
        json.dump(favourites, f, indent=2, ensure_ascii=False)


def get_weather(city): 
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"     

    try: 
        response = urllib.request.urlopen(url)         
        raw = response.read() 
        text = raw.decode("utf-8") 
        data = json.loads(text)        
        return data  
   
    except urllib.error.HTTPError as e:  
        if e.code == 404:
            print(f"City not found. Check the spelling or enter a valid City name!")
        elif e.code == 401:
            print(f"Invalid API key. Check your key on OpenWeatherMap.")
        else:
            print(f"HTTP Error: {e.code}")
            return None

    except urllib.error.URLError: 
        print("No internet connection. Check your network.")
        return None

    except json.JSONDecodeError: 
        print("Could not read the server response.")
        return None

def display_weather(data): 
    city  = data[ "name"]
    temp = data ["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]  
    condition = data["weather"][0]["description"]

    print ("\n" + "=" * 40)
    print (f"City: {city}")
    print (f"Temperature: {temp}°C")
    print (f"Feels Like: {feels_like}°C")
    print (f"Humidity: {humidity}%")
    print (f"Condition: {condition.capitalize()}")
    print ("="*40)




def get_forecast(city, units="metric"):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "units": units, "appid": API_KEY}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 404:
            print(f"City '{city}' not found.")
            return None
        if r.status_code == 401:
            print("Invalid API key.")
            return None
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def display_forecast(data, units="metric"):
    if not data or "list" not in data:
        print("No forecast data to display.")
        return
    unit_symbol = "°C" if units == "metric" else "°F"
    city_name = data.get("city", {}).get("name", "Unknown")
    print(f"\n5-day forecast for {city_name}:\n")
    print(f"{'Date/Time':<16} {'Temp':>8} {'Weather':<25}")
    print("-" * 52)
    for item in data["list"]:
        dt = datetime.fromtimestamp(item["dt"]).strftime("%m-%d %H:%M")
        temp = item["main"]["temp"]
        desc = item["weather"][0]["description"]
        print(f"{dt:<16} {temp:>6.1f}{unit_symbol}  {desc:<25}")
    print()


    
    
def get_valid_city(): 

    while True:
        city = input("Enter City name (or 'q' to exit): ")
        city = "".join(city.split())
        if city.lower() == "q":
            print("Goodbye!")
            break
        if city == "":
            print("Pls enter a city name.")
            continue
        if city.isdigit():
            print("City name cannot be numbers only. Try again.")
            continue
        if not any(c.isalpha() for c in city):
            print("City name must contain letters. Try again")
            continue
        if len(city) >  85:
            print ("City name is too long. Try again")
            continue
        return city



def manage_favourites(favourites):
    while True:
        print("\n--- Favourite Cities ---")
        print("="*40)
        if favourites:
            for i, city in enumerate(favourites, 1):
                print(f"{i}. {city}")
        else:
            print("(none saved)")
        print("\n" + "="*40)
        print("a. Add a city")
        print("r. Remove a city")
        print("v. View weather for all")
        print("b. Back to main menu")
        print("="*40)

        choice = input("Choose: ").strip().lower()

        if choice == "a":
            city = get_valid_city()
            if city and city not in favourites:
                favourites.append(city)
                print(f"Added {city}")
                save_favourites(favourites)

        elif choice == "r":
            city = input("City to remove: ").strip()
            if city in favourites:
                favourites.remove(city)
                print(f"Removed {city}")
                save_favourites(favourites)
            else:
                print("Not in favourites")

        elif choice == "v":
            for city in favourites:
                data = get_weather(city)
                if data:
                    display_weather(data)

        elif choice == "b":
            return favourites

        else:
            print("Invalid choice.")

def main():
    current_units = "metric"
    favourites = load_favourites()   # e.g. ["Lagos", "London"]

    while True:
        print("\n" + "=" * 40)
        print("       WEATHER APP")
        print("=" * 40)
        print("1. Current weather")
        print("2. 5-day forecast")
        print("3. View history")
        print("4. Favourite cities")
        print("5. Exit")
        print("=" * 40)

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            city = get_valid_city()
            if city:
                data = get_weather(city)
                if data:
                    display_weather(data)
                    save_to_history(city, data)       # history feature

        elif choice == "2":
            city = get_valid_city()
            if city:
                data = get_forecast(city, units=current_units)
                display_forecast(data, units=current_units)

        elif choice == "3":
            show_history()


        elif choice == "4":
            favourites = manage_favourites(favourites)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1-5.")



if __name__ == "__main__":
    main() 






# Without writing the code,  just explain what this is talking about, the specific steps to solve this: Weather App (Console)

    #Use a free API (e.g., OpenWeatherMap).

    #Ask for city, fetch weather, print result.

    #Skills: requests (or urllib), JSON parsing, APIs




