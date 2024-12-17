def isSafe(report):
    diffs = [report[i+1]-report[i] for i in range(len(report)-1)]
    return set(diffs).issubset({1,2,3}) or set(diffs).issubset({-1,-2,-3})


input = [x.split(' ') for x in open('day2/input.txt').read().strip().split('\n')]
input = [[int(x) for x in y] for y in input]

count = 0
for report in input:
    if isSafe(report):
        count += 1
        continue
    else:
        for i in range(len(report)):
            reportt = report[:]
            reportt.pop(i)
            if isSafe(reportt):
                count += 1
                break


print(count)


