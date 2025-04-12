# Use dictionary methods: get(), pop(), popitem(), clear(), copy().

dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(dict)
print(dict.get("name")) 
print(dict.pop("age"))
print(dict.popitem())
x = dict.copy()
print(dict.clear())
print(x)
print(dict)
