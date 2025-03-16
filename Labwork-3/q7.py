# 7. Acronym Generator
# Write a program that takes a sentence as input and generates its acronym.
# Example: "Machine Learning" → "ML"

string = input("Enter a string: ")
words = string.split()
acronym = ''.join(word[0].upper() for word in words)

print("Acronym:", acronym)