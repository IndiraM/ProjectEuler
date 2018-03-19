#Self powers
out = 0

for i in range(1,1001):
    power = i**i
    out = out +power

out = str(out)

print out[-10:]