# Използваме while True: за да четем безкрайно потребителски вход
# За всеки вход използваме оператора in, за да знаем какво да отговорим
# else-a накрая хваща случая, в който не знаем какво да отговорим
# Програмата се прекъсва с натискане на Ctrl + C

while True:
    text = input("Say what? ")

    if "hello" in text or "Hello" in text:
        print("Hello there, good stranger!")
    elif "how are you?" in text:
        print("I am fine, thanks. How are you?")
    elif "feelings" in text:
        print("I am a machine. I have no feelings")
    elif "age" in text:
        print("I have no age. Only current timestamp")
    else:
        print("Sorry, I don't understan you. Try hello, feelings or age")
