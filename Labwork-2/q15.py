# Create a nested if condition to check if a person is eligible to vote (age ≥ 18) and is a citizen.

age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18:
    if citizen == 'yes':
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")