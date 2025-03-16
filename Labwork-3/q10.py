# 10. Anagram Checker
# Write a function that checks whether two input strings are anagrams (contain the same
# letters in a different order)

def are_anagrams(str1, str2):
    # Remove any spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

