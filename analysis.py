
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

#PRECIPITATION
precipitation = data["Precipitation_mm"].mean()
avg_precipitation = data.groupby("Location")["Precipitation_mm"].mean()
print("Average Precipitation of Country: {precipitation} mm")
print(f"===Average Precipitation by Location===")
print(avg_precipitation)

locations = data["Location"].unique()
figures,axes = plt.subplots(2,2)

font = dict(fontfamily = "serif", fontsize = 10)
axes[0,0].set_title("Temperature in USA", fontfamily='serif',fontsize=12)
axes[0,0].barh(avg_temp.index,avg_temp,color='orange')
axes[0,0].set_ylabel("Cities in USA",**font)
axes[0,0].set_xlabel("Temperature in Celsius",**font)

axes[0,1].set_title("Humidity in USA", fontfamily='serif',fontsize=12)
axes[0,1].barh(avg_humidity.index,avg_humidity,color='blue')
axes[0,1].set_ylabel("Cities in USA",**font)
axes[0,1].set_xlabel("Humidity in %",**font)

axes[1,0].set_title("Wind Speed in USA", fontfamily='serif',fontsize=12)
axes[1,0].barh(avg_wind.index,avg_wind,color='green')
axes[1,0].set_ylabel("Cities in USA",**font)
axes[1,0].set_xlabel("Wind Speed in km/h",**font)

axes[1,1].set_title("Precipitation in USA", fontfamily='serif',fontsize=12)
axes[1,1].barh(avg_precipitation.index,avg_precipitation,color='purple')
axes[1,1].set_ylabel("Cities in USA",**font)
axes[1,1].set_xlabel("Precipitation in mm",**font)

plt.tight_layout()
plt.show()