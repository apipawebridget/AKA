#assignment
cities=["Mbale", "Gulu", "Mbarara", "Jinja","Mbale"]
#remove duplicates
cities=list(dict.fromkeys(cities))
print(cities)
#
cities=["Mbale", "Gulu", "Mbarara", "Jinja","Mbale"]
no_duplicates=[]
for city in cities:
    if city not in no_duplicates:
        no_duplicates.append(city)
print(no_duplicates)