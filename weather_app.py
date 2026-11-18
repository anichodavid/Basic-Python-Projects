import urllib.request   # Import the urllib.request module — used to send HTTP requests to servers


import json # Import the json module — used to convert JSON text into Python dictionaries

import os
from dotenv import load_dotenv

load_dotenv()   # loads variables from .env

 # Store the API key for OpenWeatherMap
API_KEY = os.environ.get("WEATHER_API_KEY")
if not API_KEY:
    print("❌ API key not found. Create a .env file with WEATHER_API_KEY=your_key")
    exit()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather" # Store the base URL (endpoint) for OpenWeatherMap's current weather API

def get_weather(city): # Define a function that fetches weather data for a given city


    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"     # Build the full request URL with city, API key, and metric units



    try: # Start a try block to handle potential network or HTTP errors


        response = urllib.request.urlopen(url)         # Send the HTTP request to the URL and get a response object


        raw = response.read() # Read the raw bytes from the server's response


        text = raw.decode("utf-8") # Decode the raw bytes into a UTF-8 string (JSON text)


        data = json.loads(text)         # Convert the JSON string into a Python dictionary


        return data  # Return the parsed dictionary to the caller

    
    except urllib.error.HTTPError as e:  # Catch HTTP errors (e.g., 404 Not Found, 401 Unauthorized)


        if e.code == 404:
            print(f"City not found. Check the spelling")
        elif e.code == 401:
            print(f"Invalid API key. Check your key on OpenWeatherMap.")
        else:
            print(f"HTTP Error: {e.code}")
            return None

    except urllib.error.URLError: # Catch URL errors (e.g., no internet connection, DNS failure)


        print("No internet connection. Check your network.")
        return None

    except json.JSONDecodeError: # Catch JSON decoding errors (if the response is not valid JSON)

        print("Could not read the server response.")
        return None

def display_weather(data): # Define a function that extracts the weather data from the dictionary and prints it in a readable format
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

def main(): # Define the main function that runs the app
    print ("Weather App")
    print ("="*40)
    while True:
        city = input("Enter City name (or 'q' to exit): ").strip() 
        if city.lower() == "q":
            print("Goodbye!")
            break
        if city == "":
            print("Pls enter a city name.")
            continue
        data = get_weather(city)
        if data is not None:
             display_weather(data)



if __name__ == "__main__":
    main() # Check if this file is being run directly (not imported) # Call the main function to start the app







# Without writing the code,  just explain what this is talking about, the specific steps to solve this: Weather App (Console)

    #Use a free API (e.g., OpenWeatherMap).

    #Ask for city, fetch weather, print result.

    #Skills: requests (or urllib), JSON parsing, APIs




