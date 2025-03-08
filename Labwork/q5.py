# WAP to check if a string is palindrome

samp_string = str(input("Enter your string: "))

if samp_string == samp_string[::-1]:
    print("Your string is a pallindrome")
else:
    print("Your string is not a pallindrome")
    