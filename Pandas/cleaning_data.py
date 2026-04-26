import pandas as pd 
df = pd.read_csv("globalAirQuality.csv")
print(df["country"])
print(df["aqi"])
print(df[["country","aqi"]])

#row
print(df.loc[0:1]) # slicing starting index : included last index
print(df.loc[0:2,["country","city","latitude","aqi"]])

print(df.iloc[0:3,1:5]) #slicing starting index : ending index not included
print(df.iloc[0:2,1:3])