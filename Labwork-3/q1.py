# 1. Triple Quotes 
# Create a Python program that stores a paragraph using triple quotes and extracts all
# sentences that contain a specific word. ex(extract Python containing sentences 

paragraph = """
Python is a high-level, interpreted programming language known for its simplicity and readability. 
Created by Guido van Rossum and first released in 1991, Python emphasizes code readability with its 
notable use of significant whitespace. It supports multiple programming paradigms, including procedural, 
object-oriented, and functional programming. Python's extensive standard library and vibrant community 
make it a popular choice for web development, data analysis, artificial intelligence, scientific computing, 
and more.
"""

print(paragraph)

word = input("Enter your desired word: ")

sentence = paragraph.split(".")

for sentence in sentence:
    if word in sentence:
        print(sentence)
