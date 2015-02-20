# Измислените задачи се намират тук

## Задача 1 - Блокове в Люлин

Иванчо, който живее в Люлин, е забелязал следното нещо: **всички блокове в Люлин са подредени един след друг в редица**

Иванчо знае височината на всеки един блок от тази редица и иска да знае, ако застане пред първия блок - колко блока след него ще успее да види?

Първият по-висок блок, след който следва по-нисък е последния блок, който той ще успее да види.

* Потребителят трява да въведе число, което отговаря за броя блокове в Люлински квартал в една един списък.
* После последователно трябва да въведе колко ще е висок всеки блок от списъка.


Във файл `lyulin_city.py`, напишете програма, която отпечатва на екрана колко блока ще успее да види Иванчо, ако застане в началото на редицата.


**Например**: ако имаме 5 блока по 1, 2, 5, 3, 1 етажа, Иванчо ще успее да види точно 3 блока.


## Задача 2 - Няколко  функции с числа

Във файла `int_functions.py`, напишете програма, която дефинира следните функции:

* `reverse_int(n)` - взима едно число и го връща в обърнато. Например `123` е `321`
* `sum_digits(n)` - намира сумата на всички цифри в `n`
* `product_digits(n)` - намира произведението на всички цифри в `n`

В програмата прочете едно число и отпечатайте резултатът от прилагането на горните функции върху него.

## Задача 3 - Марийка и градския транспорт

Марийка е нов студент в София и иска да сметне как най-евтино ще и излезе придвижването с градския транспорт, спрямо броя на пътуваният, която прави за 1 месец и броя на линииите, които използва.

**Знаем следните цени за 1 месец:**

* Цената на 1 билетче е 1 лев.
* Цената на 1 карта за цяла линия е 23 лева.
* Цената за всички линии е 50 лева.

Във файл `travel.py`, напишете функция `travel_cost(travels)`, където `travels` е списък от числа, представляващ следното:

* Всеки елемент в `travels` представлява броя на пътувания в 1 линия в градския транспорт.
* Например `[12, 28]` би се разчело така: Марийка е пътувала общо в 2 линии, като в 1вата е пътувала 12 пъти, а във втората 28 пъти.
* Ако имаме `[50]` имаме 50 пътувания само в 1 линич.

**Функцията трябва да върне оптималната цена, която Марийка ще плати за месеца, при тези придвижвания в `travels`**

**Например:**

* Ако имаме `travels = [28, 5]`, то ще е най-изгодно да си вземем една карта за първата линия за 23 лева, вместо да платим 28 лева за билетчета, а за втората линия да си платим 5 лева за билетчета. Тотално, 28 лева.
* Ако имаме `travels = [22]`, ще е най-изгодно да си купим 22 билетчета за 22 лева.
* Ако имаме `travels = [30, 28, 55]`, то ще е най-изгодно да си вземем карта за цялата градска мрежа


## Задача 4 - Функция, която генерира случайни числа

Във файл `random_numbers.py`, напишете функция `generate_random_list(n, start, end)`, която прави следното нещо:

* Генерира списък с `n` на брой елементи
* Всеки елемент е цяло число, което се намира в затворения интервал `[start, end]`

**Например:**

```python
>>> generate_random_list(5, 1, 3)
[1, 2, 1, 3, 1]
```

## Задача 5 - Число, чиито цифри за числа от редицата на Фибоначи

Във файл `fib_number.py`, напишете функция `fib_number(n)`, която:

* Взима едно цяло число `n`
* Връща цяло число, чииото цифри са съставени от пръвите `n` члена на редицата на Фибоначи.

Редицата на Фибоначи е много известен проблем в математиката и програмирането.

* Тя е безкрайна редица, която има следния вид: `1, 1, 2, 3, 5, 7, ....`
* Първите два елемента са `1` и `1`
* Всеки следващ елемент на редицата се получава, като се съберат предходните два.
* Например, 3тия елемент е `1 + 1 = 2`.

[Тук може да прочетете повече за редицата на Фибоначи](http://en.wikipedia.org/wiki/Fibonacci_number)

### Подсказка

1. За да решите задачата по-лесно, напишете първо функцията `fib(n)`, която връща списък с първите `n` члена на редицата на Фибоначи.
2. След това вземете този списък и го обърнете в число. Внимавайте с числата, които имат повече от 1 цифра в себе си.

За да получите първите `n` елемента от редицата на Фибоначи, може да ползвате следния алгоритъм:

1. Ако `n == 1`, то това е `[1]`
2. Ако `n == 2`, то това е `[1, 1]`
3. Ако `n == 3`, то започвате започвате чрез цикъл да получавате всеки следващ елемент, като той е равен на сумата на предходните два.
4. Всеки новополучен елемент го добавяте в резултатен списък.
5. Държите брояч, който знае колко члена на редицата сме намерило.
6. Когато този брояч стане == на `n`, тогава спираме

### Задача 1 

Във файла `c2h5oh.py`, направете списък с 5 вида алкохол.

Примерен списък е:

```python
["Rom", "Vodka", "Djin", "Beer", "Whiskey"].
```

* Програмата отпечатва списъка на потребителя и го кара да избере някои от изброените видове алкохол.
* Ако избрания алкохол не е в списъка, да се даде възможност на потребителя да избира отново.
* След това програмата пита потре - Централна маса

бителя какво количество от избрания алкохол иска да си поръча.
* Ако количеството е по-голямо от 5 чаши, изкарва надпис на потребителя `"Вие пихте достатъчно"`, ако е по-малко от 5 чаши, програмата пита потребителя дали иска още една чаша и така, докато потребителя не изпие 5 чаши.

* Когато изпие 5-тата чаша, излиза надпис `"Вие пихте достатъчно!"`
* Ако потребителя каже, че не иска да пие повече програмата отпечатва: "Довиждане" и "Вие пихте достатъчно!"
потребителя каже, че не иска да пие повече програмата отпечатва: `"Довиждане"` и `"Вие пихте достатъчно!"`

## Отбор 4 - Централна маса

### Задача 2 - Ред на Фибоначи до n ( вход от потребител ) в списък и превръщане:

* Въвеждаме от конзолата n, като n е броя на числа от реда на Фибоначи,
който искаме да принтираме
* Реда на Фибоначи започва с 1, 2 и всяко следващо число е резултат от сумата на предходните 2 числа.
* Резултатът да е представлява  списък от всички числа до n, който да се изпринтира.
* Числата от списъкът да се обърнат в число (int)

## Отбор 5

## Отбор 6

