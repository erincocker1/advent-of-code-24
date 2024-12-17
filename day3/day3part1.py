import re

multiplications = re.findall('mul\(\d{1,3},\d{1,3}\)', open('day3/input.txt').read().strip())
multiplications = [[int(x.split(',')[0].split('(')[1]), int(x.split(',')[1].split(')')[0])] for x in multiplications]
print(sum([x[0]*x[1] for x in multiplications]))