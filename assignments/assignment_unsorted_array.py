#Given an unsorted integer array, find the first missing positive integer
n=input('Enter size of the list')
i=0
list1=[]
while i<n:
    list1.append(input('Enter the Element:\n'))
    i+=1
print list1
for i in range(1,max(list1)+1):
    if i not in list1:
        print i
        break
