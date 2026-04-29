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

