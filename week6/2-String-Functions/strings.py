def string_to_char_list(string):
    result = []

    for ch in string:
        result += [ch]

    return result


def char_list_to_string(char_list):
    result = ""

    for ch in char_list:
        result += ch

    return result


def change_string(index, ch, string):
    char_list = string_to_char_list(string)

    char_list[index] = ch

    return char_list_to_string(char_list)


def reverse(items):
    result = []

    for item in items:
        result = [item] + result

    return result


def str_reverse(string):
    char_list = string_to_char_list(string)
    char_list = reverse(char_list)

    return char_list_to_string(char_list)


def str_reverse2(string):
    result = ""

    for ch in string:
        result = ch + result

    return result


print(str_reverse2("Python"))


def join(delimiter, items):
    result = ""
    last_index = len(items) - 1

    for index in range(0, last_index):
        item = items[index]
        result = result + item + delimiter

    result += items[last_index]

    return result

print(join("!!", ["Kuche", "Kotka", "Slon"]))


def take(n, items):
    result = []

    for index in range(0, min(n, len(items))):
        result += [items[index]]

    return result


def startswith(search, string):
    n = len(search)
    search_char_list = string_to_char_list(search)
    return take(n, string) == search_char_list


def endswith(search, string):
    search = str_reverse(search)
    string = str_reverse(string)

    return startswith(search, string)


def tail(items):
    result = []

    for index in range(1, len(items)):
        item = items[index]
        result += [item]

    return result


def str_drop(n, string):
    result = ""

    for index in range(n, len(string)):
        result += string[index]

    return result


def trim_left(string):
    while startswith(" ", string):
        string = str_drop(1, string)

    return string


def trim_right(string):
    return str_reverse(
                        trim_left(
                            str_reverse(string)))


def trim(string):
    result = trim_left(string)
    result = trim_right(result)

    return result
