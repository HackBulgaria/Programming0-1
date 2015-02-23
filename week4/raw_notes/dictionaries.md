# Dictionaries

In the programming world, there are always concepts, that we are using in the real world.

Dicts are one of them.

If you think about that, dictionaries represent a **mapping** between words. If it is a langauge -> language dictionary, if you want ot translate a word, you look it up in the dictionary and find the proper translation.

You have a **key** - the word you are looking for. And when you find that word, you get the **value** - the given translation.

This is the general concept of a dictionary - **a key-value mapping of some sort.**

## Lists / Arrays

In programming, so far, if we want to store multiple values under one name, we use lists.

And if we want to lookup inside the lists, we use indexes - an integer number, starting from 0.

For example:

```python
person = ["Radoslav", "Yordanov", "Georgiev"]

print(person[0])
print(person[1])
print(person[2])
```

This is great.

We create a mapping between the integers, starting from 0 and the values in the list at the given position.

But the thing, that can create many problems is the type of the index - an integer.

How can you tell what this is:

```python
configuration[3]
```

As far as we know, configuration is a list and we want the 4th element of that list.

But what is the 4th element? A password? A username? A port? No idea.

We have to go one step further, and create a variable, giving meaning to the 4th element of the configuration:

```
database_password = configuration[3]
```

Now we know that the 4th element is a database password.

But there is one more problem - the ordering of `confiugration`

Imagine that our `configuration` looks like that:

```python
configuration = ["RadoRado", "password123", "localhost:3360", "dbpassword123"]
```

And we have forgoten our database name. We can add it like that:

```python
configuration = ["RadoRado", "password123", "localhost:3360", "students", "dbpassword123"]
```

Now `configuration[3]` is no longer the db password, but the db name. We have to change that everywhere!


Now, we have the following problems:

* Lists are great but if we start to fix the position of elements, in order to know the thing that is there, we have a problem
* Also, `configuration[0]` tells us nothing about the 1st element in `configuration`. We have to create an additional variable to give proper name.
* We can map an integer to a value with a list. **But how can we map something else? Like a String to a value?**

## Enter dictionaries

In most of the modern programming languages, you will find that there is a dictionary of some sort.

This is a structure, much like lists, with one big difference: **indexes can be strings!**

In a dictionary, we talk about keys and values.

* Keys can be of type ing and string.
* Values can be of any type.

Dictionaries can be known with many names:

* Hashes
* Maps
* Hash Maps
* Associative Arrays

They all mean the same thing - mapping between a key and a value, where the type of the key can be different, from integer.

In python, we create a dictionary like that:

```
dict = {}
```

This is an empty dictionary.

We can create a dictionary with keys and values in it:

```python
configuration = {
    "username": "RadoRado",
    "password": "password123",
    "database_name": "students",
    "database_password": "db123"
}
```

As you can see, we define a pair of key-value with the `:` between them.

Keys are strings. Values can be everything.


Now, imagine that we have the `configuration` dictionary. It acts like a list, but the type of the indexes are strings:

```python
print(configuration["username"])
```

This is much better than `configuration[0]` - we have a descriptive string, telling us what is in there.

## Working with dictionaries.

Dictionaries act much like lists:

* We can change the value of a given key
* We can add new key with a value
* We can check wether a key is present in the dictionary
* Iterate over a dictionary

### Adding and Changing keys

```python
person = {}

person["name"] = "Radoslav Georgiev"
person["age"] = 24

print(person)

person["name"] = "Ivaylo Bachvarov"
print(person)
```

```python
words = {}

words["then"] = 0
words["then"] += 1

words["and"] = 2

print(words)
```

### Checking if key is present:

We can use the `in` operator with the following form:

```
key in dict
```

This returns True or False


```python
configuration = {
    "username": "RadoRado",
    "password": "password123",
    "database_name": "students",
    "database_password": "db123"
}

if "username" in configuration:
    print("We have a username key")
```

### Iterating over a dictionary

For example, lets have the `configuration` dict:

```
for key in configuration:
    print(key)
    print(configuration[key])
```

So dicts are very helpful since we can now have strings as keys.

## Complex examples

If we want to model a classroom, we can combine lists and dicts:

```python
classroom = [{ "name": "Ivan", "age": 16}, { "name": "Maria", "age": 23 }]

for student in classroom:
    print(student["name"])
    print(student["age"])
```
