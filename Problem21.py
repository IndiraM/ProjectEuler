#Amicable numbers
def divisor(n):
    sum = 1
    for i in range(2,n+1):
        if n%i==0 and i!=n:
            sum = sum+i
    return sum

result =0
for i in range(1,10000):
    out = divisor(i)
    out1 = divisor(out)
    if out1 == i and i!=out:
        result = result+i
print result


