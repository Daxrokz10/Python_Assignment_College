# Create a program that demonstrates the use of append(), pop(), and sort() methods in a list.

a = [1,22,65,91,12,3,4,5,6,7,8,9,10]
while True:
    print("1. Append")
    print("2. Pop")
    print("3. Sort")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a.append(int(input("Enter a number: ")))
    elif choice == 2:
            a.pop()
    elif choice == 3:
        a.sort()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
    
print(a)