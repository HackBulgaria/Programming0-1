def base(width, stars):
    points_count = (width - stars) // 2
    stars_string = "*" * stars
    one_side_points = "." * points_count


    return one_side_points + stars_string+ one_side_points


def clock(n):
    width = n
    while n > 0:
        print(base(width, n))
        n -= 2

    n = 3

    while n <= width:
        print(base(width, n))
        n += 2

