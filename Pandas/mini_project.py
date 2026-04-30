import pandas as pd
import kagglehub
import os

path = kagglehub.dataset_download("noopurbhatt/retail-intelligence-100k-user-behavior-dataset")
print(os.listdir(path))

df = pd.read_csv(path +"/retail_user_behavior_100k.csv")
print(df)