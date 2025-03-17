# 11. Find the Longest Word in a Sentence
# Write a function that finds the longest word in a given sentence.

def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

sentence = input("Enter a sentence: ")
longest_word = find_longest_word(sentence)
print("The longest word is:", longest_word)

