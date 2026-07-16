
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

data["Month"] = data["Date_Time"].dt.month_name()
data["Day"] = data["Date_Time"].dt.day
data["Year"] = data["Date_Time"].dt.year

#TEMPERATURE
temp = data["Temperature_C"].mean()
avg_temp = data.groupby("Location")["Temperature_C"].mean()
print(f"Average Temperature of Country: {temp} C")
print(f"===Average Temperature by Location===")
print(avg_temp)

#HUMIDITY
humidity = data["Humidity_pct"].mean()
avg_humidity = data.groupby("Location")["Humidity_pct"].mean()
print(f"Average Humidity of Country: {humidity} %")
print(f"===Average Humidity by Location===")
print(avg_humidity)

#WIND SPEED
wind_speed = data["Wind_Speed_kmh"].mean()
avg_wind = data.groupby("Location")["Wind_Speed_kmh"].mean()
print(f"Average Wind Speed of Country: {wind_speed} km/h")
print(f"===Average Wind Speed by Location===")
print(avg_wind)

#PRECIPITATION
precipitation = data["Precipitation_mm"].mean()
avg_precipitation = data.groupby("Location")["Precipitation_mm"].mean()
print(f"Average Precipitation of Country: {precipitation} mm")
print(f"===Average Precipitation by Location===")
print(avg_precipitation)

print()
print("==TEMPERATURE==")
print(f"Hottest City : {avg_temp.idxmax()} == Average Temperature : {avg_temp.max(): 2f} C")
print(f"Coldest City:  {avg_temp.idxmin()} Average Temperature : {avg_temp.min(): 2f} C")

print()
print("==HUMIDITY==")
print(f"Most Humid City : {avg_humidity.idxmax()} == Average Temperature : {avg_humidity.max(): 2f} %")
print(f"Least Humid City:  {avg_humidity.idxmin()} == Average Temperature : {avg_humidity.min(): 2f} %")

print()
print("==WIND SPEED==")
print(f"Most Windiest City : {avg_wind.idxmax()} == Average Temperature : {avg_wind.max(): 2f} km/hr")
print(f"Least Windiest City:  {avg_wind.idxmin()} == Average Temperature : {avg_wind.min(): 2f} km/hr")

print()
print("==PRECIPITATION==")
print(f"Wettest City : {avg_precipitation.idxmax()} == Average Temperature : {avg_precipitation.max(): 2f} mm")
print(f"Driest City:  {avg_precipitation.idxmin()} == Average Temperature : {avg_precipitation.min(): 2f} mm")

figures,axes = plt.subplots(2,2)

font = dict(fontfamily = "serif", fontsize = 10)
title = dict(fontfamily='serif',fontsize=12)

axes[0,0].set_title("Temperature in USA", **title)
axes[0,0].barh(avg_temp.index,avg_temp,color='orange')
axes[0,0].set_ylabel("Cities in USA",**font)
axes[0,0].set_xlabel("Temperature in Celsius",**font)

axes[0,1].set_title("Humidity in USA", **title)
axes[0,1].barh(avg_humidity.index,avg_humidity,color='blue')
axes[0,1].set_ylabel("Cities in USA",**font)
axes[0,1].set_xlabel("Humidity in %",**font)

axes[1,0].set_title("Wind Speed in USA", **title)
axes[1,0].barh(avg_wind.index,avg_wind,color='green')
axes[1,0].set_ylabel("Cities in USA",**font)
axes[1,0].set_xlabel("Wind Speed in km/h",**font)

axes[1,1].set_title("Precipitation in USA", **title)
axes[1,1].barh(avg_precipitation.index,avg_precipitation,color='purple')
axes[1,1].set_ylabel("Cities in USA",**font)
axes[1,1].set_xlabel("Precipitation in mm",**font)

plt.tight_layout()
plt.show()

fig1,ax1 = plt.subplots(2,2)

ax1[0,0].set_title("Temperature",**title)
ax1[0,0].hist(data['Temperature_C'],bins=10,edgecolor="white",color="orange")
ax1[0,0].set_ylabel("Temperature in Celcius",**font)
ax1[0,0].set_xlabel("Number of Records",**font)

ax1[0,1].set_title("Humidity",**title)
ax1[0,1].hist(data["Humidity_pct"],bins=10,edgecolor="white")
ax1[0,1].set_ylabel("Humidity in %",**font)
ax1[0,1].set_xlabel("Number of Records",**font)

ax1[1,0].set_title("Wind Speed",**title)
ax1[1,0].hist(data["Wind_Speed_kmh"],bins=10,edgecolor="white",color="green")
ax1[1,0].set_ylabel("Wind Speed in km/hr",**font)
ax1[1,0].set_xlabel("Number of Records",**font)

ax1[1,1].set_title("Precipitation",**title)
ax1[1,1].hist(data["Precipitation_mm"],bins=10,edgecolor="white",color="purple")
ax1[1,1].set_ylabel("Precipitation in mm",**font)
ax1[1,1].set_xlabel("Number of Records",**font)

plt.tight_layout()
plt.show()
