import pandas as pd
s = pd.Series([1,2,3,4,5])
print(s)

#label based access
s = pd.Series([24,25,26,27],index = ["shrajal","shakti","aditya","rishav"] )
print(s)
print(s["shrajal"])
print(s["rishav"])
print(s.index)