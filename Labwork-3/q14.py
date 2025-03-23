# Count the Occurrences of a Given Character

def count_characters(sentence, character):
    return sentence.count(character)

sentence = input("Enter a sentence: ")
character = input("Enter a character: ")
character_count = count_characters(sentence, character)
print("The number of occurrences of the character in the sentence is:", character_count)