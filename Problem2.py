#Even Fibonacci numbers

n1 = 1
n2 = 1
sum =0
out =0

if __name__ == '__main__':
    while(out<=4000000):
        sum= n1+n2
        n1=n2
        n2=sum
        print sum
        if sum%2==0:
            out = out+sum

print out


'''a, b = 1, 1
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a+b  # the real formula for Fibonacci sequence
print total'''