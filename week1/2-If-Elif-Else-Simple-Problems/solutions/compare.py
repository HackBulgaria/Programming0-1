a = input("Enter a: ")
b = input("Enter b: ")

a = int(a)
b = int(b)

if a > b:
    print("a(" + str(a) + ") is bigger than b(" + str(b) + ")!")
elif a < b:
    print("b(" + str(b) + ") is bigger than a(" + str(a) + ")!")
else:
    print("a(" + str(a) + ") is equal to b(" + str(b) + ")")
