'''Write a program that given a text file will create a new text file in which all the lines from the
original file are numbered from 1 to n(where n is the number of lines in the file).'''

fp=open('test.txt','r+')
content=fp.readlines()
fp.seek(0)
count=0
for line in content:
    count+=1
    line=str(count) + ' ' + line[0:]
    fp.writelines(line)
