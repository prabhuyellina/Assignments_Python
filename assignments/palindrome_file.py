def is_palindrome(var):
    rev_strng=reversed(var)
    if list(var)==list(rev_strng):
        print 'Palindrome is:',var

file_name=raw_input('Enter the file name')
fp=open(file_name,'r')
lines=fp.readlines()
for line in lines:
    line=line.strip('\n')
    line=line.strip(' ')
    is_palindrome(line.lower())
