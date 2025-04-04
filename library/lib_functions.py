import os
from .ai_speech import speak
import webbrowser
import sys
import requests

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def open_spotify():
    speak("Opening Spotify")
    webbrowser.open("https://open.spotify.com")

def google_search(query):
    speak(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def get_weather():
    speak("Fetching weather information")
    city = "New York"  # Change to your city or make it dynamic
    api_key = "your_openweather_api_key"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"]
        return f"The current temperature in {city} is {temp}°C."
    return "Weather information not available."

def control_system(command):
    if "shutdown" in command:
        speak("Shutting down the system")
        if sys.platform == "win32":
            os.system("shutdown /s /t 1")
        else:
            os.system("sudo shutdown now")
    elif "restart" in command:
        speak("Restarting the system")
        if sys.platform == "win32":
            os.system("shutdown /r /t 1")
        else:
            os.system("sudo reboot")