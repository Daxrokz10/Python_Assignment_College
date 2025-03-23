# Sort Words in a Sentence Alphabetically
# Write a program that sorts words in a sentence alphabetically.

def sort_words(sentence):
    words = sentence.split()
    sorted_words = sorted(words)
    return ' '.join(sorted_words)

# Example usage
sentence = input("Enter a sentence: ")
sorted_sentence = sort_words(sentence)
print("Sorted sentence:", sorted_sentence)

