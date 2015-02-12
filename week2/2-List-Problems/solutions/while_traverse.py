books = ["Learn You a Haskell", 
         "The Healthy Programmer",
         "Code Complete",
         "The Pragmatic Programmer",
         "Pro Git",
         "Introduction to Algorithms",
         "Concrete Mathematics"]

start = 0
end = len(books) - 1 # 6

while start <= end:
    book = books[start]
    print(book)

    start += 1
