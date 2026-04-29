#import pandas
import pandas as pd

#load dataset
df = pd.read_csv("IRIS.csv")

#-----------------A------------
print(df.head(10))
print("\n shape:")
print(df.shape)
print("\n summary staticis:")
print(df.describe())



#-----------------B----------
filtered = df[(df["petal_length"] > 4.5) & (df["species"] == "Iris-virginica")]
print("\n filtered data:")
print(filtered)