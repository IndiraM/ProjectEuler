def collatz(n):
    if n%2==0:
        n=n/2
    else:
        n=(3*n)+1
    return n

for i in range(1,2):
    print collatz(i)