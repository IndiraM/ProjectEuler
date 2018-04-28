def Curious_number(n):
    res = 0
    for curious in str(n):
        sum = 1
        for i in range(1,int(curious)+1):
            sum=sum*i
        res = res+sum
    #print n,res
    return res

if __name__ == '__main__':
    for number in range(3,1000000):
        out = Curious_number(number)
        #print out,number
        sum =0
        if number == out:
            print 'Pass',number
            sum =sum+number
    print sum



