# #Assianment-1
##import pandas
import pandas as pd

# #load dataset
# df = pd.read_csv("IRIS.csv")

# #-----------------A------------
# print(df.head(10))
# print("\n shape:")
# print(df.shape)
# print("\n summary staticis:")
# print(df.describe())



# #-----------------B----------
# filtered = df[(df["petal_length"] > 4.5) & (df["species"] == "Iris-virginica")]
# print("\n filtered data:")
# print(filtered)



# #----------------C-------------


# group = df.groupby("species").agg({
#     "sepal_length":"mean",
#     "petal_length":"max",
#     "sepal_width":"std"
   
# })
# print("\n group result:")
# group



# #-----------------------D-----------------
# #creating new column petal_ratio
# df["petal_ratio"] = df["petal_length"] / df["petal_width"] 
# # mean of petal_ratio
# ratio = df.groupby("species")["petal_ratio"].mean()
# #another method
# petal_rat = df.groupby("species").agg({"petal_ratio":"mean"})
# print(petal_rat)
# print(ratio)


#Assianment-2
#Task-1
df = pd.read_csv("Titanic-Dataset.csv")
selected_column = df[["Name","Age","Sex","Fare","Survived"]]
selected_column = selected_column.head()
print(selected_column)

#Task-2
passenger = df[(df["Sex"] == "female") & (df["Fare"] > 30)]
print(passenger)

#Task-3
group = df.groupby("Pclass").agg({
    "Survived":"mean",
    "Fare":"mean",
    "Age":"mean"

})
print(group)