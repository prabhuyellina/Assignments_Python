x=raw_input('Enter the string')
list1=[]
i=count=0
z=len(x)-1
while i<z:
    j=i+1
    if x[i]==x[j]:
        i+=1
        count+=1
    list1.append((x[i],count+1))
    i+=1
    if j==z:
        list1.append((x[j],count+1))
    count=0
print list1 
    

    
