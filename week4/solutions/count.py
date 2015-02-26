def count_vowels_consonants(word):
    result = {
        "vowels": 0,
        "consonants": 0
    }

    vowels =  "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    for ch in word:
        if ch in vowels:
            result["vowels"] += 1
        elif ch in consonants:
            result["consonants"] += 1

    return result

print(count_vowels_consonants("aaaAcccD"))

