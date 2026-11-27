import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import requests

API_KEY = os.environ.get("WEATHER_API_KEY")

# ─────────────────────────────────────────────
# API functions (same as your console app)
# ─────────────────────────────────────────────

def get_weather(city, units="metric"):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "units": units, "appid": API_KEY}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 404:
            return {"error": f"City '{city}' not found."}
        if r.status_code == 401:
            return {"error": "Invalid API key."}
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}

def get_forecast(city, units="metric"):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "units": units, "appid": API_KEY}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 404:
            return {"error": f"City '{city}' not found."}
        if r.status_code == 401:
            return {"error": "Invalid API key."}
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}

# ─────────────────────────────────────────────
# Formatting helpers (return strings, don't print)
# ─────────────────────────────────────────────

def format_current(data, units="metric"):
    if "error" in data:
        return f"{data['error']}"
    sym = "°C" if units == "metric" else "°F"
    city = data.get("name", "Unknown")
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    return (
        f" {city}\n"
        f" Temperature: {temp:.1f}{sym} (feels like {feels:.1f}{sym})\n"
        f" Conditions: {desc}\n"
        f" Humidity: {humidity}%\n"
        f" Wind: {wind} m/s\n"
    )

def format_forecast(data, units="metric"):
    if "error" in data:
        return f" {data['error']}"
    if "list" not in data:
        return " No forecast data."
    sym = "°C" if units == "metric" else "°F"
    city = data.get("city", {}).get("name", "Unknown")
    lines = [f" 5-day forecast for {city}:\n"]
    lines.append(f"{'Date/Time':<16} {'Temp':>8}  Weather")
    lines.append("-" * 50)
    for item in data["list"]:
        dt = datetime.fromtimestamp(item["dt"]).strftime("%m-%d %H:%M")
        temp = item["main"]["temp"]
        desc = item["weather"][0]["description"]
        lines.append(f"{dt:<16} {temp:>6.1f}{sym}  {desc}")
    return "\n".join(lines)

# ─────────────────────────────────────────────
# GUI
# ─────────────────────────────────────────────

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nacho_Weathers")
        self.root.geometry("720x560")
        self.units = tk.StringVar(value="metric")

        # ── Top row: city entry + search button ──
        top = ttk.Frame(root, padding=10)
        top.pack(fill="x")

        ttk.Label(top, text="City:").pack(side="left")
        self.city_entry = ttk.Entry(top, width=30)
        self.city_entry.pack(side="left", padx=(5, 10))
        self.city_entry.bind("<Return>", lambda e: self.show_current())  # Enter key

        ttk.Button(top, text="Search", command=self.show_current).pack(side="left")

        # ── Units radio buttons ──
        units_frame = ttk.Frame(root, padding=(10, 0))
        units_frame.pack(fill="x")
        ttk.Label(units_frame, text="Units:").pack(side="left")
        ttk.Radiobutton(units_frame, text="Celsius", variable=self.units,
                        value="metric").pack(side="left", padx=5)
        ttk.Radiobutton(units_frame, text="Fahrenheit", variable=self.units,
                        value="imperial").pack(side="left", padx=5)

        # ── Action buttons ──
        btns = ttk.Frame(root, padding=(10, 5))
        btns.pack(fill="x")
        ttk.Button(btns, text="Current Weather",
                   command=self.show_current).pack(side="left", padx=(0, 5))
        ttk.Button(btns, text="5-Day Forecast",
                   command=self.show_forecast).pack(side="left", padx=(0, 5))
        ttk.Button(btns, text="Clear",
                   command=self.clear).pack(side="left")

        # ── Results area (scrollable) ──
        result_frame = ttk.Frame(root, padding=10)
        result_frame.pack(fill="both", expand=True)

        self.result = tk.Text(result_frame, wrap="word", font=("Courier", 10))
        scrollbar = ttk.Scrollbar(result_frame, command=self.result.yview)
        self.result.configure(yscrollcommand=scrollbar.set)

        self.result.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ── Status bar ──
        self.status = ttk.Label(root, text="Ready", relief="sunken", anchor="w")
        self.status.pack(fill="x", side="bottom")

    # ── helpers ──

    def _get_city(self):
        city = self.city_entry.get().strip()
        city = " ".join(city.split())      # same normalization as console
        if not city:
            messagebox.showwarning("Missing city", "Please enter a city name.")
            return None
        return city

    def _write(self, text):
        self.result.delete("1.0", "end")
        self.result.insert("end", text)

    def _set_status(self, text):
        self.status.config(text=text)

    # ── actions ──

    def show_current(self):
        city = self._get_city()
        if not city:
            return
        self._set_status(f"Fetching current weather for {city}…")
        self.root.update_idletasks()
        data = get_weather(city, units=self.units.get())
        self._write(format_current(data, units=self.units.get()))
        self._set_status("Done" if "error" not in data else data["error"])

    def show_forecast(self):
        city = self._get_city()
        if not city:
            return
        self._set_status(f"Fetching forecast for {city}…")
        self.root.update_idletasks()
        data = get_forecast(city, units=self.units.get())
        self._write(format_forecast(data, units=self.units.get()))
        self._set_status("Done" if "error" not in data else data["error"])

    def clear(self):
        self.result.delete("1.0", "end")
        self._set_status("Cleared")


if __name__ == "__main__":
    root = tk.Tk()
    WeatherApp(root)
    root.mainloop()