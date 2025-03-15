# Write a program to reverse a list using a loop.

a = [1, 2, 3, 4, 5]
b = []
i = len(a)-1
while i >= 0:
    b.append(a[i])
    i -= 1
print(b)