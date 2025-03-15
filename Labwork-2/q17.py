# Create a program that prints the multiplication table of a given number using a for loop.

a = int(input("Enter a number: "))
i = 1
while i<=10:
    print(a, "x", i, "=", a*i)
    i += 1