# WAP to find a matching element from the list

list = [1,2,3,4,5,6]
num = int(input("Enter the value of element you want to find: "))
i=1

while i<len(list):
    if num == list[i]:
        print(num , 'found at' , list[i])
        break
    else:
        print("Searching")
    i+=1
    