#1000-digit Fibonacci number
n1 = 1
n2 = 1
count = 10
sum =0
res = []

res.append(n1)
res.append(n2)
if __name__ == '__main__':
    for i in range(1,11111):
        sum= n1+n2
        res.append(int(sum))
        n1=n2
        n2=sum

res = map(int,res)
#print res

def retrunOutput():
    for out in res:
        out = str(out)
        if len(out)==1000:
            return out
        else:
            'Invalid output'
Output = retrunOutput()


print str(res.index(int(Output))+1)


