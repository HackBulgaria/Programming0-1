# Обобщение на Демо-денят за Програмиране 0

## Какво е променлива?

Променлива е нещо, което има следния вид: `име = стойност`

Връзваме стойността с някакво име. И може да променяме стойността за това име. Например:

```python
a = 5
a = a + 1
print(a)
```

Създаваме променливата `a`, която има стойност `5`, след което променяме стойността и, като взимаме старата такава и я увеличаваме с 1.

## Стойността има тип (type):

Видяхме, че различните стойности има различни типове:

* Integer (цяло число): `a = 5`
* String (Низ, текст): `a = "Python"` - огбраждаме с кавички.
* Boolean (Истина или лъжа): `a = True` (`a = 5 == 5`)

**В Python няма нищо, което може да стане имплицитно (Помните ли тази дума?)**

Какво става, когато направим:

* `5 + 5? # 10`
* `"5" + 5? # (TypeError)`
* `"5" + "5" # "55"`

**+-а знае как да:**

* Събира две числа
* Събира два string-a

**Как събираме число със String?**

Трябва **експлицитно** (Помните ли тази дума?) да превърнем едното към другото:

* `"5" + 5 = "5" + str(5) = "55"`
* `"5" + 5 = int("5") + 5 = 10`

На какво е равно:

`str(int("5")) == "5"`


##  Какво е интерпретатор, компилатор и REPL?

Python се интерпретира и има REPL (Read Evaluate Print Loop)

**Как пишем Python? Имаме 2 варианта:**

* В REPL-то, пишем ред по ред и се изпълнява
* В текстов файл с разширение `.py` и я изпълняваме:

Ако имаме `hello.py`:

`$ python hello.py`

Виждаме неща на конзолата, само ако имаме `print` в програмата.

## Констукции в езика

### if конструкция - чрез нея взимаме решения.

"Ако това е така, направи нещо, иначе направи нещо друго"

```python
if expression:
    print("This is executed when expression is True")
else:
    print("This is executed when expression is False")
```

Където `expression` е нещо, което се свежда до булева стойност. Вижте това -https://github.com/HackBulgaria/Programming0-1/blob/master/problems.md#%D0%A7%D0%B0%D1%81%D1%82-%D1%87%D0%B5%D1%82%D0%B2%D1%8A%D1%80%D1%82%D0%B0-%D0%98%D1%81%D1%82%D0%B8%D0%BD%D0%B0-%D0%B8-%D0%9B%D1%8A%D0%B6%D0%B0

if-a има и конструкция, която ни позволява да вземем повече от 1 решение:

```python
if expression1:
    print("This is executed when expression1 is True")
elif expression2:
    print("This is executed when expression2 is True")
elif expression3:
    print("This is executed when expression3 is True")
else:
    print("This is executed when expression1, 2 and 3 are False")
```

## Неща за продължаване

За да продължите да пишете Python, ние препоръчваме 2 неща:

* Книгата Learn Python The Hard Way - http://learnpythonthehardway.org/book/
* Codecademy с Python - http://www.codecademy.com/tracks/python

**Курсът по Програмиране 0 ще започне Януари месец 2015. Ще пишем допълнтелно за това :)**
