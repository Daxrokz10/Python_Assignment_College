# 10. Anagram Checker
# Write a function that checks whether two input strings are anagrams (contain the same
# letters in a different order)

def are_anagrams(str1, str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    
    if sorted(str1) == sorted(str2):
        print("is anagram")
    else:
        print("isnt anagram")

str1 = "hi"
str2 = "ii"

are_anagrams(str1,str2)