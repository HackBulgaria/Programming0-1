# Задачи с низове

Низовете също са много често срещани в програмирането. За да боравим успешно с тях е хубаво да напишем няколко функции за работа с тях.

Низовете донякъде представляват списъци.

* Поддържат достъп на елемент по индекс
* Могат да се обхождат с for
* Функцията `len` работи и върху низове, връщайки тяхната дължина
* Не могат обаче да променят стойността си по индекс.

Ето примери:

```python
>>> str = "Python"
>>> str[0]
'P'
>>> str[1]
'y'
>>> str[0] = "P"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: 'str' object does not support item assignment
>>> for ch in str:
....    print(ch)
....
P
y
t
h
o
n
```

Стринговете поддържат операция, наречена **конкатенация** - слепяне на два низа. Тя се извършва чрез оператора `+`. Това е начинът, за боравене с низове, ако искаме да създадем нов низ.

За пример, ако имаме функцията `change_at(index, ch, string)`, която замества буквата на позиция `index` с `ch` в `string`, то ние ще я имплементираме така:

```python
def change_at(index, ch, string):
    result = ""
    n = len(string)

    for str_index in range(0, n):
        if str_index == index:
            result += ch
        else:
            result += string[str_index]

    return result
```

Във файла `strings.py`, напишете следните функции:

## str_reverse

Същата функция, като `reverse` за списъци, само че обръща string наобратно:

```python
>>> str_reverse("Python")
"nohtyP"
>>> str_reverse("kapak")
"kapak"
>>> str_reverse("")
""
```

## join

Една от най-полезните функциии, която ще използваме много, когато боравим с низове в функцията `join(delimiter, items)`

* `delimiter` е произволен низ
* `items` е списък от неща
* Функцията трябва да върне низ, който представлява всеки елемент от `items`, разделен посредата с `delimiter`

Например: `join(" ", ["Hello", "there"])` ще прозведе стринга `"Hello there"`, слагайки `" "`, между всеки два елемента, без да слага пред първия и след последния елемент.

Бъдете сигурни, че конкатегирате низове. Минете всеки елемент от `items` през `str` функцията, която взима някакъв произволен тип и връща string.

Тогава ще може да направим: `join("|", [1, 2, 3])`, което ще даде резултат `"1|2|3"`

Например:

```python
>>> join(" ", ["Radoslav", "Yordanov", "Georgiev"])
'Radoslav Yordanov Georgiev'
>>> join("\n", ["line1", "line2"])
'line1\nline2'
>>> print(join("\n", ["line1", "line2"]))
line1
line2
```

## startswith

Напишете функцията `startswith(search, string)`, която проверява дали `string`, започва с низа `search`.

Например:

```python
>>> startswith("Py", "Python")
True
>>> startswith("py", "Python")
False
>>> startswith("baba", "asdbaba")
False
```

## endswith

Напишете функцията `endswith(search, string)`, която проверява дали `string` завършва с низа `search`.

Например:

```python
>>> endswith(".py", "hello.py")
True
>>> endswith("kapak", "babakapak")
True
>>> endswith(" ", "Python   ")
True
>>> endswith("py", "python")
False
```

Опитайте се да решите тази функция чрез `reverse` и `startswith`

## trim

Друга много полезна функция.

Когато работим с низове, прочетени от потребител, много често имаме **whitespace** (шпации) в началото и в края на низа.

Пример:

```python
"   asda   "
" spacious    "
"no here but yes at end   "
```

Това е излишен шум, който само ще ни попречи да работим добре с низовете.

Напишете полената функция `trim(string)`, която маха всички **whitespace** символи от началото и от края на `string`, но запазва тези `whitespace`-ове вътре в самия `string`

Например:

```python
>>> trim("   asda   ")
'asda'
>>> trim(" spacious    ")
'spacious'
>>> trim("no here but yes at end   ")
'no here but yes at end'
>>> trim("                      ")
''
>>> trim("python")
'python'
```
