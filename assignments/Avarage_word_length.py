''' Write a program that will calculate the average word length of a text stored in a file
(i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens)'''

fp=open('test.txt','r')
word_count=1
char_count=0
for line in fp.readlines():
    char_count+=len(line)
    for data in line:
        if data==' ' or data=='\n':
            word_count+=1
print char_count
print 'Average word length is %d' %(char_count/word_count)