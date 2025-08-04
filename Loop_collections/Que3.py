l1 = [1,2,4,3,6,8,5,7,9,10,11]
l2 = []
even=[]
odd=[]
for i in l1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
i,j=0,0
while i<len(even) and j<len(odd):
    l2.append(even[i])
    l2.append(odd[j])
    i+=1
    j+=1
    
print(l2)