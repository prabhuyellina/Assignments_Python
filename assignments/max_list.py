def max_list(list1):
    return reduce(lambda a,b:a if a>b else b,list1)

print max_list([5,8,1,0,7,2,9,8])
