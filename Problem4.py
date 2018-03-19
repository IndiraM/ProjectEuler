largest = []
for i in range(100,1000):
    for j in range(100,1000):
        sum = i*j
        sum = str(sum)
        if sum == sum[::-1]:
            largest.append(int(sum))
largest.sort()

print largest[-1]





