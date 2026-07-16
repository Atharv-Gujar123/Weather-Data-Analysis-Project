import matplotlib.pyplot as plt
import pandas as pd
import calendar
#LOAD DATASET
data = pd.read_csv('Weather/archive/weather_data.csv',nrows=1000)
data["Date_Time"] = pd.to_datetime(data["Date_Time"])
print("===Original Data===")
print(data.head())
print(data.info())
print(data.describe())

def show_average(column):
    return data[column].mean()

def location_average(location,column):
    return data.groupby(location)[column].mean()

#DATA CLEANING
data.fillna({
    "Precipitation_mm":0,
    "Temperature_C":data["Temperature_C"].mean(),
    "Wind_Speed_kmh":data["Wind_Speed_kmh"].mean(),
    "Humidity_pct":data["Humidity_pct"].mean()
}, inplace=True)

data["Month"] = data["Date_Time"].dt.month
data["Day"] = data["Date_Time"].dt.day
data["Year"] = data["Date_Time"].dt.year

def monthly_avg(column):
    results = {}
    grouped = data.groupby(["Location","Month"])[column].mean()
    for x in data["Location"].unique():
        results[x] = grouped.loc[x]
    return results
monthly_temp = monthly_avg("Temperature_C")
monthly_rain = monthly_avg("Precipitation_mm")

# MONTHLY ANALYSIS

print("=== MONTHLY TEMPERATURE ===")
print(monthly_temp)
print()
print("=== MONTHLY PRECIPITATION ===")
print(monthly_rain)
print()

#TEMPERATURE
temp = show_average("Temperature_C")
avg_temp = location_average("Location","Temperature_C")
print(f"Average Temperature of Country: {temp:.2f} C")
print(f"===Average Temperature by Location===")
print(avg_temp)

#HUMIDITY
humidity = show_average("Humidity_pct")
avg_humidity = location_average("Location","Humidity_pct")
print(f"Average Humidity of Country: {humidity:.2f} %")
print(f"===Average Humidity by Location===")
print(avg_humidity)

#WIND SPEED
wind_speed = show_average("Wind_Speed_kmh")
avg_wind = location_average("Location","Wind_Speed_kmh")
print(f"Average Wind Speed of Country: {wind_speed:.2f} km/h")
print(f"===Average Wind Speed by Location===")
print(avg_wind)

#PRECIPITATION
precipitation = show_average("Precipitation_mm")
avg_precipitation = location_average("Location","Precipitation_mm")
print(f"Average Precipitation of Country: {precipitation:.2f} mm")
print(f"===Average Precipitation by Location===")
print(avg_precipitation)

# SUMMARY STATISTICS

print()
print("==TEMPERATURE==")
print(f"Hottest City : {avg_temp.idxmax()} == Average Temperature : {avg_temp.max():.2f} C")
print(f"Coldest City:  {avg_temp.idxmin()} Average Temperature : {avg_temp.min():2f} C")

print()
print("==HUMIDITY==")
print(f"Most Humid City : {avg_humidity.idxmax()} == Average Humidity : {avg_humidity.max():.2f} %")
print(f"Least Humid City:  {avg_humidity.idxmin()} == Average Humidity : {avg_humidity.min():.2f} %")

print()
print("==WIND SPEED==")
print(f"Most Windiest City : {avg_wind.idxmax()} == Average Wind Speed : {avg_wind.max():.2f} km/hr")
print(f"Least Windiest City:  {avg_wind.idxmin()} == Average Wind Speed : {avg_wind.min():.2f} km/hr")

print()
print("==PRECIPITATION==")
print(f"Wettest City : {avg_precipitation.idxmax()} == Average Precipitation : {avg_precipitation.max():.2f} mm")
print(f"Driest City:  {avg_precipitation.idxmin()} == Average Precipitation : {avg_precipitation.min():.2f} mm")

corr = data[["Temperature_C","Humidity_pct","Wind_Speed_kmh","Precipitation_mm"]].corr()
font = dict(fontfamily = "serif", fontsize = 10)
title = dict(fontfamily='serif',fontsize=12)



# VISUALIZATIONS
for city,values in monthly_temp.items():
    plt.plot(values.index,values.values,label=city,marker="o")
    months = [calendar.month_abbr[m] for m in values.index]
    plt.xticks(values.index,months)
plt.grid()
plt.title("Monthly Average Temperature",**title)
plt.xlabel("Months",**font)
plt.ylabel("Temperature in Celsius",**font)
plt.legend(ncol=2)
plt.tight_layout()
plt.show()

for city,values in monthly_rain.items():
    plt.plot(values.index,values.values,label=city,marker="o")
    months = [calendar.month_abbr[m] for m in values.index]
    plt.xticks(values.index,months)
plt.grid()
plt.title("Monthly Average Precipitation",**title)
plt.xlabel("Months",**font)
plt.ylabel("Precipitation in mm",**font)
plt.legend(ncol=2)
plt.tight_layout()
plt.show()

figures,axes = plt.subplots(2,2)

axes[0,0].set_title("Average Temperature by City", **title)
axes[0,0].barh(avg_temp.index,avg_temp,color='orange')
axes[0,0].set_ylabel("Cities in USA",**font)
axes[0,0].set_xlabel("Temperature in Celsius",**font)

axes[0,1].set_title("Average Humidity by City", **title)
axes[0,1].barh(avg_humidity.index,avg_humidity,color='blue')
axes[0,1].set_ylabel("Cities in USA",**font)
axes[0,1].set_xlabel("Humidity in %",**font)

axes[1,0].set_title("Average Wind Speed by City", **title)
axes[1,0].barh(avg_wind.index,avg_wind,color='green')
axes[1,0].set_ylabel("Cities in USA",**font)
axes[1,0].set_xlabel("Wind Speed in km/h",**font)

axes[1,1].set_title("Average Precipitation by City", **title)
axes[1,1].barh(avg_precipitation.index,avg_precipitation,color='purple')
axes[1,1].set_ylabel("Cities in USA",**font)
axes[1,1].set_xlabel("Precipitation in mm",**font)

plt.tight_layout()
plt.show()

fig1,ax1 = plt.subplots(2,2)

ax1[0,0].set_title("Temperature Distribution",**title)
ax1[0,0].hist(data['Temperature_C'],bins=10,edgecolor="white",color="orange")
ax1[0,0].set_xlabel("Temperature in Celsius",**font)
ax1[0,0].set_ylabel("Frequency",**font)

ax1[0,1].set_title("Humidity Distribution",**title)
ax1[0,1].hist(data["Humidity_pct"],bins=10,edgecolor="white")
ax1[0,1].set_xlabel("Humidity in %",**font)
ax1[0,1].set_ylabel("Frequency",**font)

ax1[1,0].set_title("Wind Speed Distribution",**title)
ax1[1,0].hist(data["Wind_Speed_kmh"],bins=10,edgecolor="white",color="green")
ax1[1,0].set_xlabel("Wind Speed in km/hr",**font)
ax1[1,0].set_ylabel("Frequency",**font)

ax1[1,1].set_title("Precipitation Distribution",**title)
ax1[1,1].hist(data["Precipitation_mm"],bins=10,edgecolor="white",color="purple")
ax1[1,1].set_xlabel("Precipitation in mm",**font)
ax1[1,1].set_ylabel("Frequency",**font)

plt.tight_layout()
plt.show()

plt.figure(figsize=(6,5))
plt.imshow(corr,cmap="turbo")
plt.colorbar()
plt.clim(-1,1)
plt.title("Correlation Matrix",**title)
plt.xticks(range(len(corr.columns)),corr.columns,rotation=25,**font)
plt.yticks(range(len(corr.columns)),corr.columns,**font)

for x in range(len(corr.columns)):
    for y in range(len(corr.columns)):
        plt.text(y,x,f"{corr.iloc[x,y]:.2f}", ha="center",va="center")
plt.tight_layout()
plt.show()
