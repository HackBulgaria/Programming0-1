example = [1, 2, 3]

n = len(example)

for i in range(0, n):
    for j in range(i + 1, n):
        x = example[i]
        y = example[j]
        print(x, y)

