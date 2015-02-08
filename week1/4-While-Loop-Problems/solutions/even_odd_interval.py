lower_bound = input("Enter lower bound for interval: ")
upper_bound = input("Enter upper bound for interval: ")

lower_bound = int(lower_bound)
upper_bound = int(upper_bound)

while lower_bound <= upper_bound:
    # Това е поредното число от интервала
    n = lower_bound

    if n % 2 == 0:
        print(str(n) + " - even")
    else:
        print(str(n) + " - odd")

    # Това е съкратен запис за lower_bound = lower_bound + 1
    lower_bound += 1
