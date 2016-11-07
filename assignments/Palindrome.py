def is_palindrome(var):
    i=0
    j=len(var)-1
    while i<=j:
        if var[i]==var[j]:
            pass
            if i==j:
                print 'Palindrome'
        else:
            print 'Not a Palindrome'
            break
        i+=1
        j-=1

is_palindrome(raw_input('Enter the string'))