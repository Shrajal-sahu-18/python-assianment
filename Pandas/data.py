import pandas as pd

# df = pd.read_csv("raw_data.csv")
# print(df)

# # df = pd.read_json("empolyee_data.json")
# # print(df)

# #methods in pandas
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

# # practice problem
# age_mean = df["age"].mean()
# cleaned_data = df.copy()
# cleaned_data["age"] = cleaned_data["age"].fillna(age_mean)


#type converstion
df = pd.read_csv("raw_data.csv") 
print(df)
print(df.dtypes)
df2 = df.copy()
df2 = df2.fillna(0)
df2["age"]  = df2["age"].astype("int64")
print(df2,df2.dtypes)