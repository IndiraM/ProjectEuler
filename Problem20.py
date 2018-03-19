
def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum*i
    return sum
out = factorial(100)
print out

count = []
for i in str(out):
    count.append(i)
print sum(map(int,count))
