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
print("\n total users:\n",total_users)
print("\n total_events:\n",total_events)


#Top product
print("\n Top 10 viewed product:\n")
print(df[df["event_type"] == "view"]["product_id"].value_counts().head(10))
print("\n Top 10 purchased prodcut:\n")
print(df[df["event_type"] == "purchase"]["product_id"].value_counts().head(10))


#category anaylsis
print("\n Top category: \n")
print(df.groupby("category")["event_type"].count().sort_values(ascending = False).head(10))


#Brand analysis
print(df[df["event_type"] == "purchase"]["brand"].value_counts().head(10))

#average price per brand
print("\n avarage price per brand: \n")
print(df.groupby("brand")["price"].mean().sort_values(ascending = False).head(10))

#new column
df["Month"] = df["timestamp_utc"].dt.month_name()
df["timestamp_utc"].dt.month.unique()

# Activity
print("\n monthly activity: \n")
df.groupby("Month")["event_type"].count()

print("\n Hourly activity:\n")
df["Hour"] = df["timestamp_utc"].dt.hour
print(df.groupby("Hour")["event_type"].count())



#conversional funnel

view = df[df["event_type"] == "view"]["user_id"].nunique()
cart = df[df["event_type"] == "add_to_cart"]["user_id"].nunique()
purchase = df[df["event_type"] == "purchase"]["user_id"].nunique()

print("\n user funnel:\n")
print("views:",view)
print("add_to_cart:",cart)
print("purchase:",purchase)

conversion_rate = purchase/view
print("\nconversion_rate:",conversion_rate)


#Repeat customer
repeat_customer = df[df["event_type"] == "purchase"]["user_id"].value_counts()
repeat_customer = repeat_customer[repeat_customer > 1]
print("\n repeated customer:\n",len(repeat_customer))