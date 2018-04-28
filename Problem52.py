def perumated_mulitples(n1,n2):
    number = set(str(n1))
    square_number = set(str(n2))
    if number == square_number:
        return True

if __name__ == '__main__':
    n = 1
    while n<=1000000:
        square = n*2
        square3 = n*3
        square4 = n * 4
        square5 = n * 5
        square6 = n * 6
        if perumated_mulitples(n,square) and perumated_mulitples(n,square3) and perumated_mulitples(n,square4) and perumated_mulitples(n,square5) and perumated_mulitples(n,square6)==True:
            print n
            break
        else:
            n = n+1
