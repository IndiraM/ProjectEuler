prime = []

for num in range(2,200000):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        prime.append(num)

print prime
print prime[10001]