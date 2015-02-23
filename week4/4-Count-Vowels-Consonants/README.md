# Брой на гласни и съгласни

Във файл `count.py` напишете функция `count_vowels_consonants(word)`, която:

* Взима един низ `word`
* Връща речник, в който има два ключа - `"vowels"` и `"consonants"`
* Срещу всеки ключ, трябва да стои съответния брой на гласни и съгласни букви в думата.

Бройте както главните, така и малките гласни и съгласни букви:

* Гласните са `"aeiouyAEIOUY"`
* Съгласните са `"bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"`

**Например:**

```python
>>> count_vowels_consonants("aaaAcccD")
{
  "vowels": 4,
  "consonants": 4
}
```
