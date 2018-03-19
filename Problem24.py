from itertools import permutations


l = [0,1,2,3,4,5,6,7,8,9]
#l = [0,1,2]
out = []

p = permutations(l)

for i in p:
    out.append(i)

#print out
res =  str(out[999999]).replace(', ','')
print res


