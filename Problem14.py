def Collatz(n):
    if n%2==0:
        n=n/2
        return n
    else:
        n=(3*n)+1
        return n


n = 13
while(n!=1):
    Collatz(n)

