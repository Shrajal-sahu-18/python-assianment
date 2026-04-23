import pandas as pd 

# DataFrame

info = {
    "name":["alice","bob","charlie"],
    "age":[20,21,21],
}
df = pd.DataFrame(info)
print(df)