for a in range(1,100000):
    b = a*2
    c= a*3
    d= a*4
    e= a*5
    f= a*6

    def num(n):
        Sorted_list = []
        for i in n:
            Sorted_list.append(i)
            Sorted_list.sort()
        return Sorted_list

    a1= num(str(a))
    a2= num(str(b))

    if cmp(a1,a2) == 0:
        print True
