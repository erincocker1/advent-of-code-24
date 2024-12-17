directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

w = open('day4/input.txt').read().strip().split('\n')

count = 0
for i in range(len(w)):
    for j in range(len(w[0])):
        if w[i][j] == 'X':
            for d in directions:
                indices = [i+d[0], j+d[1], i+2*d[0], j+2*d[1], i+3*d[0], j+3*d[1]]
                if min(indices) < 0 or max(indices) >= 140:
                    continue
                if w[i+d[0]][j+d[1]] == 'M' and w[i+2*d[0]][j+2*d[1]] == 'A' and w[i+3*d[0]][j+3*d[1]] == 'S':
                    count += 1

print(count)

