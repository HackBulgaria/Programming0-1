def setify(a):
    pass


def diff(a, b):
    pass


def union(a, b):
    pass


def intersection(a, b):
    pass


def cartesian_product(a, b):
    # Tuple is (a, b) as a syntax
    pass


def main():
    print(setify([0, 1, 1, 5, 5, 6]) == [0, 1, 5, 6])
    print(union([0, 0, 0, 0, 0], [1, 2]) == [0, 1, 2])
    print(intersection([0, 0, 1, 2, 5], [5, 5, 6]) == [5])
    print(diff([0, 1, 2, 3, 4, 5], [0, 0, 1, 1, 2, 2, 3, 3]) == [4, 5])
    print(cartesian_product([0, 1], [1]) == [(0, 1), (1, 1)])


if __name__ == '__main__':
    main()
