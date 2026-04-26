import pandas as pd 
df = pd.read_csv("globalAirQuality.csv")
print(df["country"])
print(df["aqi"])
print(df[["country","aqi"]])

#row
print(df.loc[0:1]) # slicing starting index : included last index

#cells-row_column
print(df.loc[0:2,["country","city","latitude","aqi"]])

print(df.iloc[0:3,1:5]) #slicing starting index : ending index not included
print(df.iloc[0:2,1:3])

print(df.at[0,"city"]) #print single value
print(df.iat[0,3])

#copy create karna
cities = df["city"].copy()
cities[0] = "mumbai"
print(cities)


#filtiring data
clean_data = df.copy()
# clean_data= clean_data[clean_data["aqi"]>=100]
# print(clean_data)
clean_data = clean_data[(clean_data["aqi"]>=100) & (clean_data["temperature"]>=30)][["aqi","city"]]
# print(clean_data)
print(clean_data)
