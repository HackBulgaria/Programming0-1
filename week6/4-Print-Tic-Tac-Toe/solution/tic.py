def join(delimiter, items):
    result = ""
    last_index = len(items) - 1

    for index in range(0, last_index):
        item = items[index]
        result = result + item + delimiter

    result += items[last_index]

    return result

# Това е първа стъпка
def board_to_string(board):
    result = []
    
    for row in board:
        stringed_row = join("|", row)
        result += [stringed_row]

    return join("\n", result)

board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]

result = board_to_string(board)
print("1st step result:")
print("======")
print(result)
print("======")


# Това е втората стъпка
def board_to_string2(board):
    result = []
    
    for row in board:
        stringed_row = join(" | ", row)
        result += [stringed_row]

    return join("\n", result)

board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]

result = board_to_string2(board)
print("2st step result:")
print("======")
print(result)
print("======")


# Това е третата стъпка
def board_to_string3(board):
    result = []
    
    for row in board:
        stringed_row = join(" | ", row)
        stringed_row = "| " + stringed_row + " |"
        result += [stringed_row]

    return join("\n", result)

board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]

result = board_to_string3(board)
print("3st step result:")
print("======")
print(result)
print("======")
