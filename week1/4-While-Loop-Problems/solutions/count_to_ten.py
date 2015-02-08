start = 1
end = 10

print("Counting from 1 to 10")

while start <= end:
    print(start)

    # С това условие си гарантираме, че няма да зациклим безкрайно
    start = start + 1

# А сега обратното броене
print("Counting from 10 to 1")

start = 10
end = 1

while start >= end:
    print(start)

    start = start - 1
