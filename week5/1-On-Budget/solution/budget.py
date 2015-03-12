def on_budget(books, budget):
    result = {
        "books_on_budget": 0,
        "loan": 0
    }

    count = 0
    total_price = sum(books)
    books = sorted(books)

    for book in books:
        if budget - book < 0:
            break

        budget -= book
        total_price -= book
        count += 1

    result["books_on_budget"] = count
    result["loan"] = max(0, total_price - budget)

    return result

print(on_budget([0, 10, 100, 5, 3, 8, 25], 35))
print(on_budget([0, 0, 0], 10))
print(on_budget([50, 60, 10], 20))
