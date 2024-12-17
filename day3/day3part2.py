import re
pattern = 'mul\(\d{1,3},\d{1,3}\)'

m = open('day3/input.txt').read().strip().split("don't()")
do = re.findall(pattern,m.pop(0))
m = [x.split("do()") for x in m]
for i in range(len(m)):
    for j in range(1,len(m[i])):
                   do += re.findall(pattern, m[i][j])



do = [[int(x.split(',')[0].split('(')[1]), int(x.split(',')[1].split(')')[0])] for x in do]
print(sum([x[0]*x[1] for x in do]))