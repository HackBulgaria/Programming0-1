start = input("Enter start: ")
start = int(start)

end = input("Enter end: ")
end = int(end)

# Този път друга променлива, за да не загубим първоначалната стойност на start
counter = start

print("Counting from " + str(counter) +  " to " + str(end))

while counter <= end:
    print(counter)

    # С това условие си гарантираме, че няма да зациклим безкрайно
    counter = counter + 1

# А сега обратното броене
# Имаме и start и end и може да ги ползваме като променливи
print("Counting from " + str(end) +" to " + str(start))

# Докато края е по-голям или равен на старта, принтим
while end >= start:
    print(end)

    end = end - 1
