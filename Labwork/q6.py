# WAP to find the frequency of an element provided by user in the list

list = [1,2,3,4,5,6,3,3,3,3]
num = int(input("Enter the value of element you want to find: "))
i=1
count=0
while i<len(list):
    if num == list[i]:
        print(num , 'found at' , 'list ',i)
        count += 1
        
    else:
        print("Searching")
    i+=1

print(num,' is found',count,'times')
    