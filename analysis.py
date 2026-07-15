import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Weather/archive/weather_data.csv',nrows=1000)
data["Date_Time"] = pd.to_datetime(data["Date_Time"])
print("===Original Data===")
print(data.head())
print(data.info())
print(data.describe())

data.fillna({
    "Precipitation_mm":0,
    "Temperature_C":data["Temperature_C"].mean(),
    "Wind_Speed_kmh":data["Wind_Speed_kmh"].mean(),
    "Humidity_pct":data["Humidity_pct"].mean()
}, inplace=True)

data["Month"] = data["Date_Time"].dt.month
data["Day"] = data["Date_Time"].dt.day

#TEMPERATURE
temp = data["Temperature_C"].mean()
avg_temp = data.groupby("Location")["Temperature_C"].mean()
print("Average Temperature of Country: {temp} C")
print(f"===Average Temperature by Location===")
print(avg_temp)

#HUMIDITY
humidity = data["Humidity_pct"].mean()
avg_humidity = data.groupby("Location")["Humidity_pct"].mean()
print("Average Humidity of Country: {humidity} %")
print(f"===Average Humidity by Location===")
print(avg_humidity)

#WIND SPEED
wind_speed = data["Wind_Speed_kmh"].mean()
avg_wind = data.groupby("Location")["Wind_Speed_kmh"].mean()
print("Average Wind Speed of Country: {wind_speed} km/h")
print(f"===Average Wind Speed by Location===")
print(avg_wind)
