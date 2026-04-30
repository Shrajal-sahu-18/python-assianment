#====================
#import library
import pandas as pd
import kagglehub
import os

path = kagglehub.dataset_download("noopurbhatt/retail-intelligence-100k-user-behavior-dataset")
print(os.listdir(path))
#=====================
#Load file
df = pd.read_csv(path +"/retail_user_behavior_100k.csv")

#=====================
# Task-1 
#Basic_info
#=====================
#Task - 1  Basic Info 
print("\n shape:",df.shape)
print("\n columns:", df.columns)
print("\n Info:",df.info())
print("\n First Five Rows:",df.head(5))

#data cleaning
#=====================
#mising value
print("\n missing value\n", df.isnull().sum())

#drop missing value row
df = df.dropna()