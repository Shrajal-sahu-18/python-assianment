import pandas as pd

df = pd.read_csv("raw_data.csv")
print(df)

# df = pd.read_json("empolyee_data.json")
# print(df)

#methods in pandas
print(df.head())  #first five row
print(df.tail())  #last five rows
print(df.sample(5)) #for random value
print(df.info()) #for information
print(df.shape) #row and column
print(df.describe) #for details
print(df.columns) #for columns
print(df.nunique()) #for unique value

df.isnull()
df.isna()
df.isnull().sum()
df.dropna() #empty row drop
df.dropna(axis=1)
df.fillna(0)