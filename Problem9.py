#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
start = 100
n = 600
suml = []

for i in range(start,1000):
    for j in range(i,1000-i):
        for k in range(j,1000-j):
            sum = i+j+k
            if sum == 1000:
                cond = (i ** 2)+(j ** 2)
                if cond == (k**2):
                    suml.append(i*j*k)
                    suml.append(j)
                    suml.append(k)

print suml