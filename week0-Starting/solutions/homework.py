# В тази променлива ще държим броя на книгите
book_counter = 0

book1_title = "Pragmatic Thinking and Learning"
book1_price = 30
book_counter = book_counter + 1

book2_title = "Learn You A Haskell"
book2_price = 0
book_counter = book_counter + 1

book3_title = "The Healthy Programmer"
book3_price = 50
book_counter = book_counter + 1

book4_title = "Code Complete"
book4_price = 60
book_counter = book_counter + 1

book5_title = "The Pragmatic Programmer"
book5_price = 20
book_counter = book_counter + 1

book6_title = "Pro Git"
book6_price = 0
book_counter = book_counter + 1

book7_title = "Introduction to Algorithms"
book7_price = 80
book_counter = book_counter + 1

book8_title = "Concrete Mathematics"
book8_price = 100
book_counter = book_counter + 1

print("==== Listing all books: ====")

print(book1_title + " with price: " + str(book1_price))
print(book2_title + " with price: " + str(book2_price))
print(book3_title + " with price: " + str(book3_price))
print(book4_title + " with price: " + str(book4_price))
print(book5_title + " with price: " + str(book5_price))
print(book6_title + " with price: " + str(book6_price))
print(book7_title + " with price: " + str(book7_price))
print(book8_title + " with price: " + str(book8_price))

print("==== Total sum of all: ====")
total_sum = book1_price + book2_price + book3_price + book4_price + book5_price + book6_price + book7_price + book8_price

print(total_sum)

print("==== Count of all books: ====")
print(book_counter)

discount = 0.25
price_without_discount = book8_price + book7_price

print("==== 25% discount for Introduction to Algorithms and Concrete Mathematics ====")
print(price_without_discount - (price_without_discount * discount))

print("==== Budget of 150: ====")
print("Free books:")
print(book2_title)
print(book6_title)

print("Taking books:")
print(book5_title)
print(book1_title)
print(book3_title)

print("For a total of:")
print(book5_price + book1_price + book3_price)
