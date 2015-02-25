person = {
    "name": "Rado",
    "age": 24,
    "hobbies": ["Programming", "Snowboarding", "Public speaking"]
}


# Happy Birthday!
person["age"] += 1

# Add one more hobby
person["hobbies"] += ["Waling in the park"]

if "friends" not in person:
    # Add friends list
    person["friends"] = ["Ivo", "Maria"]

for key in person:
    value = person[key]

    print(key, value)
