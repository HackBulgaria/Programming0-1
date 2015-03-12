first_name = input("Enter first name: ")
middle_name = input("Enter second name: ")
last_name = input("Enter last name: ")
birth_year = input("Enter year of birth: ")
birth_year = int(birth_year)

person = {}

person["first_name"] = first_name
person["middle_name"] = middle_name
person["last_name"] = last_name
person["birth_year"] = birth_year
person["age"] = 2015 - birth_year
