# 9. Word Censorship
# Write a function that replaces every occurrence of a banned word in a sentence with *****.
# Example: "Python is fun, but Java is difficult" (banned word: "Java") →
# "Python is fun, but ***** is difficult"

def censor_word(paragraph, banned_word):
    return paragraph.replace(banned_word, "****")

paragraph = "Python is fun, but Java is difficult"
banned_word = "Java"

censored_paragraph = censor_word(paragraph, banned_word)
print("Censored paragraph:", censored_paragraph)