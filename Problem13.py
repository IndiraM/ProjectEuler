FileList = []
sum = 0
with open("13.txt",'r') as f:
    FileRead = f.readlines()
    for lines in FileRead:
        out = lines[0:10]
        print out
        sum = sum +int(out)


print int(sum)