#Sum square difference

sum = 0
sum1 = 0

for i in range(1,101):
    square = i**2
    sum = sum +square
    sum1 = sum1+i

difference = (sum1**2)-sum
print difference
