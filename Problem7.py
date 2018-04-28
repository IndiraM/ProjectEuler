prime = []

for num in range(2,15):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        prime.append(num)

print prime
#print prime[10001]