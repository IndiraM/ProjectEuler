def pentagon(n):
    pen = (n * ((3 * n) - 1)) / 2
    return pen

pen = []
for n in range(1,3000):
    pen.append(pentagon(n))

for i in range(1000,3000):
    for j in range(1000,3000):
        a = pentagon(i)
        b = pentagon(j)

        sum = a+b
        if (a>b):
            difference = a-b
        else:
            difference = b-a
        if sum in pen and difference in pen:
            print a-b
            if (a>b):
                print a-b
            else:
                print b-a