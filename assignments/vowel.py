def vowel_check(ch):
    list1=['a','e','i','o','u']
    if ch in list1:
        return'True'
    return 'False'

print vowel_check(raw_input('Enter the Character'))
