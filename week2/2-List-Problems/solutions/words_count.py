# Събираме си целият наличен вход
# В списъка words имаме всички нужни думи
# След което го обхождаме и при всяко срещане на думата, която търсим
# Увеличаваме броячът с 1

search_word = input("Enter word: ")
n = input("Enter count of words: ")
n = int(n)

input_count = 1
words = []

while input_count <= n:
    word = input("Enter word: ")
    words = words + [word]

    input_count += 1

# Почваме да търсим броя на срещанията на search_word в words
word_count = 0

for word in words:
    if search_word == word:
        word_count += 1

print(search_word + " is found: " + str(word_count) + " times")
