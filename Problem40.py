list1 = []
for i in range(1,10000000):
    list1.append(i)

d1 = list1[1-1]
d10 = list1[10-1]
d100 = list1[100-1]
d1000 =list1[1000-1]
d10000 =list1[10000-1]
d100000 =list1[100000-1]
d1000000 =list1[1000000-1]

res = d1*d10*d100*d1000*d10000*d100000*d1000000
print res