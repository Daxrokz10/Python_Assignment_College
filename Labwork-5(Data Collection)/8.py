t=(1,1,2,3,4,5,6,7,8,9,10)
print(t)
i=0
print('First even number in the tuple is on indes:')
while i<len(t):
    if t[i]%2==0:
        print('Index: ',i,' Value: ',t[i])
        break
    i+=1
print('End of program')