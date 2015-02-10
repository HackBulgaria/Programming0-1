# Задачи със списъци

## Задача 1 - Обхождане на списък.

В два различни файла - `for_traverse.py` и `while_traverse.py`, напишете обхождане на следния списък:

```python
books = ["Learn You a Haskell", 
         "The Healthy Programmer",
         "Code Complete",
         "The Pragmatic Programmer",
         "Pro Git",
         "Introduction to Algorithms",
         "Concrete Mathematics"]
```

* Едното обхождане трябва да е с `for ... in` обхождането
* Второто обхождане трябва да е с `while`
* Обхожданията трябва да отпечатат на екрана името на всяка книга на нов ред.

## Задача 2 - Четене на променлив брой вход от потребителя.

Във файл `read_n_numbers.py` имаме следната програма:

```python

n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    numbers = numbers + [number]

    count += 1

print(numbers)
```

По този начин може да прочетем променлив брой вход от потребителя.

**Въведи числото `n` и на следващите `n` реда ще има по 1 число**

**Пуснете програмата и я разучете!**

## Задача 3 - Броят на четните числа от всички въведени от потребителя.

Във файл `only_evens.py`, напишете програма, която:

* Чете едно число `n` от потребителя
* На следващите `n` реда чете по едно число
* Първо, програмата изкарва на екрана броят на четните числа.
* Накрая принтира на екрана само четните числа, от въведените от потребителя

**Пример:**

```
Enter n: 5
2
5
6
8
9
Count of evens: 3
Evens are:
2
6
8
```

## Задача 4 - Сумата на всички числа, въведени от потребителя

Във файл `sum_numbers.py`, напишете програма, която:

* Чете едно число `n` от потребителя
* На следващите `n` редам чете по едно число от потребителя
* Накрая изкарва сумата на всички числа, които потребителят е въвел.

**Пример**

```
Enter n: 5
1
5
-10
20
0
The sum is: 16
```

## Задача 5 - Максималното число, въведено от потребител.

Във файл `max_of_n.py`, напишете програма, която:

* Чете едно число `n` от потребителя.
* На следващите `n` реда, чете по едно число от потребителя.
* Накрая изкарва максималното число от всички въведени.

**Примери:**

```
Enter n: 6
-10
20
-30
5
0
100
Max is: 100
```

## Задача 6 - Минималното число, въведено от потребител.

Във файл `min_of_n.py`, напишете програма, която:

* Чете едно число `n` от потребителя.
* На следващите `n` реда, чете по едно число от потребителя.
* Накрая изкарва мининалното число от всички въведени.

**Примери:**

```
Enter n: 6
-10
20
-30
5
0
100
Min is: -30
```

## Задача 7 - Средно-аритметично от всички въведени числа.

Във файл `avg.py`, напишете програма, която:

* Чете едно число `n` от потребителя.
* На следващите `n` реда чете по едно число от потребителя.
* Накрая изкарва средното аритметично на всички въведени числа.

Средното аритметично се определя като **разделим сумата на всички числа върху техния брой**

**Примери:**

```
Enter n: 4
1
3
2
7
Avg is 3.25
```

## Задача 8 - Брой на срещания на дадена дума.

Във файл `words_count.py`, напишете програма, която:

* Чете на един ред от потребителя, дадена дума (string) `word`
* Чете на следващия ред от потребителя едно число `n`
* На следващите `n` реда, чете по 1 дума на ред.
* Накрая, програмата изкарва броя на срещанията на думата `word` в тези `n` думи въведени от потребителя.

**Примери:**

```
Enter word: python
Enter n: 5
haskell
ruby
python
python
Go

python is found 2 times.
```

## Задача 9 - Имена, подредени по азбучен ред.

Във файл `sorted_names.py`, напишете програма, която:

* Чете едно число `n` от потребителя
* На следващите `n` реда чете по 1 име от потребителя (string)
* Накрая, програмата отпечатва всички въведени имена, подредени по азбучен ред в нарастващ ред (от a нагоре)

**Може да разгледате какво прави функцията `sorted` в Python. Работи над списъци.**

**Примери:**

```
Enter n: 5
Rado
Ivo
Maria
Lora
Anna
Sorted names are:
Anna
Ivo
Lora
Maria
Rado
```

## Задача 10 - Най-голямото и най-малкото число с едни и същи цифри.

Във файла `large_and_small.py` напишете програма, която:

* Чете едно цяло число `n` от потребителя
* На екрана извежда **най-голямото число**, което може да се получи със същите цифри от `n`
* На екрана извежда **най-малкото число**, което може да се получи със същите цифри от `n`

`n` може да е произволно голямо число, като направете решение за число, в което няма да цифрата 0.

**Примери:**

```
Enter n: 12311984324
Largest: 98443322111
Smallest: 11122334489