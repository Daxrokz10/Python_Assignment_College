# 3. String Concatenation
# Write a function that takes two strings and concatenates them with a space in between. If the
# second string is empty, return only the first string

def concatenate_strings(str1,str2):
    if  str2 == "":
        return str1
    else:
        return  str1 + " " +  str2
    
string1 =str(input("Enter the first string: "))
string2 =str(input("Enter the second string: "))
print(concatenate_strings(string1,string2))