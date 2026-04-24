import pandas as pd

df = pd.read_csv("raw_data.csv")
print(df)

# df = pd.read_json("empolyee_data.json")
# print(df)

#methods in pandas
print(df.head())  #first five row
print(df.tail())  #last five rows
print(df.sample(5)) #for random value
