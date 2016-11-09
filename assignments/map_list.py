''' Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
Write it in three different ways: 1) using a for-loop, 2) using the higher order function
map(), and 3) using list comprehensions.'''

def map_list(list1):
    list2=[]
    for word in list1:
        list2.append((word,len(word)))
    return list2

def map_function(list1):
    list2=[]
    list2=map((lambda x:(x,len(x))),list1)
    return list2

def list_comp(list1):
    list2=[]
    list2=[(x,len(x)) for x in list1]
    return list2

print map_list(['hai','How','hello','a'])
print map_function(['hai', 'How', 'hello', 'a'])
print list_comp(['hai', 'How', 'hello', 'a'])
