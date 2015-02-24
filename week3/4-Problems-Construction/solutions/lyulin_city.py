# Решението е следното:
# Винаги броим първия блок
# Пазим най-високия блок, който сме видели до момента
# След това, ако намерим блок, който е по-голям от него, броим го
# И сменяме новия най-голям блок.
def solution(blocks):
    if len(blocks) == 0:
        return 0

    seen = 1
    current_max = blocks[0]

    for block in blocks:
        if block > current_max:
            seen += 1
            current_max = block

    return seen

n = input()
n = int(n)

blocks = []
start = 1

while start <= n:
    height = input()
    heihgt = int(height)

    blocks = blocks + [height]

    start += 1

print(solution(blocks))
