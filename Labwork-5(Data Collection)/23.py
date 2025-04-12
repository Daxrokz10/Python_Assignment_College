# Count character frequency in a string using a dictionary.


def count_chars(string):
    char_dict = {}
    for char in string:
        if char.lower() in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

string = "Hello World" 

print(count_chars(string))