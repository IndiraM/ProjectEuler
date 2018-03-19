start = 2
end = 101
out = []

remove_duplicates = set()
output = []

for i in range(start,end):
    for j in range(start,end):
        res = i**j
        out.append(res)
        out.sort()


for remove in out:
    if remove not in remove_duplicates:
        remove_duplicates.add(remove)


print len(remove_duplicates)

