set1 = set()
set2 = set()
set3 =set()

for i in range(1,100000):
    T = (i*(i+1))/2
    P = (i*((3*i)-1))/2
    H = (i*((2*i)-1))

    set1.add(T)
    set2.add(P)
    set3.add(H)

print set1&set2&set3
