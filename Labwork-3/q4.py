# 4. String Methods
# Create a function that:
# ● Centers a string within 30 spaces (center()).
# ● Replaces vowels in a string with '*' (replace()).

def center_string(string):
    return string.center(30)

def replace_vowel(string):
    vowels = "aeiouAEIOU"
    for i in vowels:
        string = string.replace(i, '*')
    return string

string = "Hello world"
print("Centered string:", center_string(string))
print("String with vowels replaced:", replace_vowel(string))