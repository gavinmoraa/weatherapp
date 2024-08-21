import requests
from tkinter import *

# Function to get weather data
def get_weather():
    city = city_text.get().strip()  # Remove any leading/trailing spaces
    print(f"City entered: '{city}'")  # Debugging print statement
    api_key = '69917702e0619bde294de71662d52dd1'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    print(f"Request URL: {base_url}")  # Debugging print statement
    response = requests.get(base_url)
    weather_data = response.json()
    print(weather_data)  # Debugging print statement

    if weather_data['cod'] == 200:
        temperature = weather_data['main']['temp']
        weather = weather_data['weather'][0]['description']
        result = f'{city.capitalize()}: {temperature}°C, {weather}'
    else:
        result = f'City {city} not found.'

    weather_label.config(text=result)

# GUI setup
app = Tk()
app.title("Weather App")
app.geometry("300x200")

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack(pady=10)

get_weather_btn = Button(app, text="Get Weather", command=get_weather)
get_weather_btn.pack(pady=10)

weather_label = Label(app, text="")
weather_label.pack(pady=20)

app.mainloop()
