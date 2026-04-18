import json
cities = {
    "delhi":1000000,
    "mumbai":2000000,
    "banglore":300000
}

with open("cities.json","w") as f:
    json.dump(cities,f)

with open("cities.json","r") as f:
    data = json.load(f)

print("cities and their population:")
for city,pop in data.items():
    print(city,":",pop)
new_city = input("enter new city:")
new_population = int(input("enter population:"))
data[new_city] = new_population
with open("cities.json","w") as f:
    json.dump(data,f)

print("data updated successfully!")
print(data)

