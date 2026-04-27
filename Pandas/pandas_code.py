import pandas as pd
df = pd.read_csv("raw_data.csv")

df2 = df.copy()
new_column = [col for col in df2.columns if col != "id"] +["id"]
df2 = df2[new_column]
print(df2)