import json

def load_data(filename):
    with open(filename,"r") as f:
        data = json.load(f)
    return data
data = load_data("data.json")
print(data,type(data))

#clean and structure the data
def clean_data(data):
    unique_users = set()
    cleaned_users = []
    text_to_num = {"one":1,"two":2,"three":3,"four":4,"five":5}
    for user in data:
        raw_rating = user["rating"].strip().lower()
        if raw_rating in text_to_num:
            raw_rating = text_to_num[raw_rating]
        user["rating"] = raw_rating
        print(user)

        #missing data
        raw_age = user.get("age")
        if (raw_age == None):
            user["age"] = None


        if (user["name"].strip() in unique_users):
            continue
        unique_users.add(user["name"])
        cleaned_users.append(user)
    return cleaned_users
data = clean_data(data)
print(data)


#meaningfull insights
def get_insights(data):
    tot_rating = 0
    for user in data:
        tot_rating+=float(user["rating"])
    print(f"avg_rating = {tot_rating/len(data)}")

    #percentage of user with low rating
    poor_rating = 0
    for user in data:
        if (float(user["rating"])<3):
            poor_rating+=1
    print(f"percentage of user with poor rating = {poor_rating/len(data)*100}")
get_insights(data)


def get_recommendations(data):
    recomdations = []
    for user in data:
        current_recom = {}
        current_recom["name"] = user["name"]
        if (float(user["rating"]))<=4:
            current_recom["brand"] = ["apple"]
        else:
            current_recom["brand"] = ["samsung"]

        recomdations.append(current_recom) 
    return recomdations
get_recommendations(data)
print(get_recommendations(data))



        
