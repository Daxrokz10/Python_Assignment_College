# Remove duplicate dictionaries from a list based on a key.

dict_list = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "John", "age": 30},
    {"name": "Doe", "age": 22}
]

unique_dicts = {frozenset(d.items()): d for d in dict_list}.values()
print(list(unique_dicts))