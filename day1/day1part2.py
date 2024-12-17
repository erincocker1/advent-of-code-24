nums = [[int(x.split('   ')[0]), int(x.split('   ')[1])] for x in open('day1/input.txt').read().strip().split('\n')]
leftlist = sorted([x[0] for x in nums])
rightlist = sorted([x[1] for x in nums])
print(sum([x*rightlist.count(x) for x in leftlist]))