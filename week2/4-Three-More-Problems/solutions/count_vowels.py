# Използваме факта, че in може да търси дали низ се намира в низ
# В случая имаме един низ с всички възможни гласни
# И като ходим character по character, просто сравняваме там

vowels = "aeiouyAEIOUY"
count = 0

string = input("Enter string: ")

for ch in string:
    if ch in vowels:
        count += 1

print(count)
