# WAP to check if a list is palindrome

list = [1,2,3,2,1]

list1 = list.copy()
list1.reverse()

if list == list1:
    print("List is a pallindrome")

else:
    print("List isn't a pallindrome")