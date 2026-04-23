import pandas as pd
s = pd.Series([1,2,3,4,5])
print(s)

#label based access
s = pd.Series([24,25,26,27],index = ["shrajal","shakti","aditya","rishav"] )
print(s)
print(s["shrajal"])
print(s["rishav"])
print(s.index)

#index based access
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([1,2,3,4,5])
print(s1+s2)
s1[1] = 100
print(s1)
changed_s1 = s1.drop(1)
print(s1)
print(changed_s1)