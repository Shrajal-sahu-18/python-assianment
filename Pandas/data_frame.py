import pandas as pd 

# DataFrame

info = {
    "name":["alice","bob","charlie"],
    "age":[20,21,21],
}
df = pd.DataFrame(info)
print(df)

#dataframe with dictionary
info = {
    "name":["alice","bob","charlie"],
    "age":[20,21,22],
    "gpa":[7.9,7.5,9.0]
}
df = pd.DataFrame(info)
print(df)
print(df.index)
print(df.columns)


#DataFrame with list 

df = pd.DataFrame([["bob",21],["alice",22],["charlie",23]],columns = ["name","age"])
print(df)



#DataFrame with numpy array
import numpy as np
np_arr = np.array([[1,2,3],[4,5,6]])
df = pd.DataFrame(np_arr,columns = ["a","b","c"])
print(df)