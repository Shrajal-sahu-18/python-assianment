import pandas as pd 
df = pd.read_csv("globalAirQuality.csv")
print(df["country"])
print(df["aqi"])
print(df[["country","aqi"]])

#row
print(df.loc[0:1])
print(df.loc[0:2,["country","city","latitude","aqi"]])