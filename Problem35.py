def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


sum=0
if __name__ == '__main__':
    for i in range(2,2000000):
        if isprime(i):
            sum =sum +i

    print sum