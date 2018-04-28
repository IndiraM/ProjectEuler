from itertools import permutations

currency = 1,2,5,10,50,100,200

print type(currency)

out =permutations(currency)
for i in out:
    print i