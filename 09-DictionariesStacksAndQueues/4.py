person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}
person["surname"] = "Nowak"
person["married"] = False
person["gender"] = "male"
person["hobby"] = ["swimming", "excurions","biking"]
person["phone"] = {"landline":"123444321","mobile":"777888999", "work":"325456542"}

for key, value in person.items():
    print(f"The{key} of the person is/are {value}")