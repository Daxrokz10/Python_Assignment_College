t=(1,2,3,4,5,6,7,8,9,10)
sum=int(input('Enter the sum: '))
i=0
print(t)
print('Targeted Sum:',sum)
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i]+t[j]==sum:
            print('Pairs of numbers:',t[i],t[j])
            