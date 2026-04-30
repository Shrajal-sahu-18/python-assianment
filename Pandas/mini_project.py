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

#convert time
df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"])

#drop duplicate
df = df.drop_duplicates()
print("\n clean data shape:\n",df.shape)

#event anaylsic
df = df.rename(columns ={"user_action":"event_type"})
print("\n evevts_counts:\n",df["event_type"].value_counts())

#basic matrics
total_users = df["user_id"].nunique()
total_events = df.shape[0]