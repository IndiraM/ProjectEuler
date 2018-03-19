'''Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?'''
FileRead = open("names.txt","r")
Word_list = []
string ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for words in FileRead.read().split(','):
    Word_list.append(words.replace('"',''))
    Word_list.sort()

sumOf = 0
tot=0
Result=0

for names in Word_list:
    tmp = []
    for i in names:
        sumOf=string.index(i) + 1
        tmp.append(sumOf)
    total =  sum(tmp)
    index = (Word_list.index(names)) + 1
    Result = Result+(total*index)
print Result