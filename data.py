import json

def load_data(filename):
    with open(filename,"r") as f:
        data = json.load(f)
    return data
data = load_data("data.json")
print(data,type(data))

#clean and structure the data
def clean_data(data):
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
clean_data(data)

        
