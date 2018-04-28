#Coded triangle numbers

alpha ={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
names_list = open('names.txt','r')
def triangle(n):
    sum = (n*(n+1))/2
    return sum
triangle_list = []
for i in range(1,50):
    triangle_list.append(triangle(i))

result = 0
for words in names_list.read().split(','):
    words = words.replace('"','')
    count = 0
    for w in words:

        word_value =  alpha[w]
        count = count + word_value
    #print words+'-->'+str(count)
    if count in triangle_list:
        result = result+1

print result



