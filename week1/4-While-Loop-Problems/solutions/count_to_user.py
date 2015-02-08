n = input("Enter number: ")
n = int(n)

start = 1
end = n

print("Counting from 1 to " + str(n))

while start <= end:
    print(start)

    # С това условие си гарантираме, че няма да зациклим безкрайно
    start = start + 1

# А сега обратното броене
print("Counting from " + str(n) +" to 1")

start = n
end = 1

while start >= end:
    print(start)

    start = start - 1
