# Count the occurrences of a specific character in a given string.

string = "Hello, World!"
i=0
count = 0
target = "l"
while(i < len(string)):
    if string[i] == target:
        count += 1
    i += 1

print(count)