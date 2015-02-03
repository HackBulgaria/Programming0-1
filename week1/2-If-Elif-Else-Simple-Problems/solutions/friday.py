import time

today = time.strftime("%A")

if today == "Friday":
    print("It is Friday!")
else:
    print("It is not Friday :( Today is " + today)
