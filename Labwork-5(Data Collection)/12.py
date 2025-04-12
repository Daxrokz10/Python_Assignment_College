t=tuple(input('Enter tuples: ').split(','))
dis={}
for i in t:
    if i in dis:
        dis[i]+=1
    else:
        dis[i]=1
print('Frequency of elements in the tuple:',dis)        