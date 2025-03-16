# 2. Slicing String 
# Write a function that extracts and prints the first half and second half of a given string separately.

string = "Hello, World!"

length = int(len(string)/2)

print("First half of the string: ")
print(string[0:length])

print("Second half of the string: ")
print(string[length:])