def hash_them(keys, values):
    result = {}
    
    index = 0

    for key in keys:
        if index < len(values):
            result[key] = values[index]
        else:
            result[key] = None

        index += 1

    
    return result


print(hash_them(["key"], ["value"]))
print(hash_them(["key1", "key2"], ["value1"]))
