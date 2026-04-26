import pandas as pd 
df = pd.read_csv("globalAirQuality.csv")
print(df["country"])
print(df["aqi"])
print(df[["country","aqi"]])