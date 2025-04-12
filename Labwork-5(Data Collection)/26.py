# Merge two dictionaries and calculate average marks.

dict1={
    "John": 85,
    "Jane": 90,
    "Doe": 78
}
dict2={
    "Alice": 95,
    "Bob": 88,
    "Charlie": 82
}


dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)