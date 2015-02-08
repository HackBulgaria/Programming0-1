n = input("Enter number: ")
n = int(n)

start = 1
# Това е стъпката, с която ще ходим в start
step = 2

while start <= n:
    print(start)
    start += step
