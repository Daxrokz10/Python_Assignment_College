# Write a program to demonstrate the use of break and continue statements in loops.

while True:
    print("1. Break")
    print("2. Continue")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        break
    elif choice == 2:
        continue
    elif choice == 3:
        break
    else:
        print("Invalid choice")