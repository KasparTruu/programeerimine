person = {
    "first_name": "Kaspar",
    "last_name": "Truu",
    "birth_year": 2007,
    "location": "Rohu",
    "favorite_dessert": "Pasta",
}

print(person.get("location"))
print(person["location"])

person["favorite_dessert"] = "jäätis"

for key in person:
    print(key)

for value in person.values():
    print(value)

if "isikukood" in person:
    print("Isikukood on leitud ja olemas!")
else:
    print("Isikukoodi ei eksisteeri.")

print(len(person))

person["height"] = "190cm"
del person["birth_year"]

person.clear()