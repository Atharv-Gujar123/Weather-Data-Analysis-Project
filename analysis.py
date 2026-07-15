import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Weather/archive/weather_data.csv',nrows=1000)

print("===Original Data===")
print(data.head())
print(data.info())
print(data.describe())
