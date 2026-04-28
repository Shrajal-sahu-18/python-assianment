import pandas as pd

df = pd.read_csv("raw_data.csv")
# print(df)

# df = pd.read_json("empolyee_data.json")
# print(df)

# # #methods in pandas
# print(df.head())  #first five row
# print(df.tail())  #last five rows
# print(df.sample(5)) #for random value
# print(df.info()) #for information
# print(df.shape) #row and column
# print(df.describe) #for details
# print(df.columns) #for columns
# print(df.nunique()) #for unique value

# df.isnull()
# df.isna()
# df.isnull().sum()
# df.dropna() #empty row drop
# df.dropna(axis=1)
# df.fillna(0)

# # # # practice problem
# age_mean = df["age"].mean()
# cleaned_data = df.copy()
# cleaned_data["age"] = cleaned_data["age"].fillna(age_mean)


# # #type converstion
# df = pd.read_csv("raw_data.csv") 
# print(df)
# print(df.dtypes)
# df2 = df.copy()
# df2 = df2.fillna(0)
# df2["age"]  = df2["age"].astype("int64")
# print(df2,df2.dtypes)

# print(df["gender"].str.lower())
# print(df["gender"].str.upper())
# print(df["gender"].str.capitalize())
# print(df["name"].str.split(" "))
# print(df["country"].str.contains("US"))
# print(df["country"].str.contains("india", case=False))

# df = pd.read_csv("globalAirQuality.csv")
# df["timestamp"] = pd.to_datetime(df["timestamp"])
# print(df["timestamp"].dtypes)

# date_str = pd.Series([pd.to_datetime("2026-12-31")])
# print(type(date_str.dtypes))

# print(df)
# df2 = df.copy()
# df2["tax"] = df2["income"].apply(lambda x:"20%" if x>=50000 else "10%")
# df2["gender"] = df2["gender"].fillna("Unknown")
# gender_age = {"Male":"M","Female":"F","Unknown":"U"}

# df2["gender"] = df2["gender"].map(gender_age)
# df2 = df2.assign(new_income = df2["income"] * 1.1)
# df2["country"] = df2["country"].replace("USA","US")
# df2.columns = ["Id","Name","Age","Country","Gender","Income","Tax","New_income"]
# df2.rename(columns = {"income":"salary"})
# df2.rename(index = {1:"one"})
# df2.sort_values("income")
# df2.sort_values("income" ,ascending= False)

# #reset
# df2.reset_index()
# df2.reset_index(drop = True)

#practice task

# df2 = df.copy()
# df2 = df2.drop_duplicates()
# df2 = df2.fillna(0)
# df2 = df2.sort_values("income")
# df2 = df2.reset_index(drop = True)
# df2 = df2.to_csv("sorted_data.csv")
# print(df2)

print(df.groupby("gender")["income"].mean())
print(df.groupby("gender")["income"].min())
print(df.groupby("gender")["income"].max())