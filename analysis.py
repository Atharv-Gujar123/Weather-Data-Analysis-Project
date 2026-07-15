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

print(data.head())
