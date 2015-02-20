n = input("Enter n: ")
n = int(n)

print("Now turning number into digits")

digits = []

while n != 0:
    digit = n % 10
    digits = [digit] + digits
    n = n // 10

print(digits)
print("Now turning digits to number")

n_again = 0

for digit in digits:
    n_again = n_again * 10 + digit

print(n_again)
