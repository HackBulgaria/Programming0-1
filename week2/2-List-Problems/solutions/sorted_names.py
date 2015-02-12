n = input("Enter count of names: ")
n = int(n)

count = 1
names = []

while count <= n:
    name = input("Enter name: ")
    names = names + [name]

    count += 1

# Тук използваме функцията sorted
names = sorted(names)

for name in names:
    print(name)
