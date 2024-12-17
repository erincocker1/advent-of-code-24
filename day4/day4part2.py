directions = [[(2,0),(1,1),(0,2),(2,2)],[(0,-2),(1,-1),(2,0),(2,-2)],[(-2,0),(-1,-1),(0,-2),(-2,-2)],[(0,2),(-1,1),(-2,0),(-2,2)]]
#in order, relative positions of M, A, S, S

w = open('day4/input.txt').read().strip().split('\n')

count = 0
for i in range(len(w)):
    for j in range(len(w[0])):
        if w[i][j] == 'M':
            for d in directions:
                indices = [i+d[0][0], j+d[0][1], i+d[1][0], j+d[1][1], i+d[2][0], j+d[2][1], i+d[3][0], j+d[3][1]]
                if min(indices) < 0 or max(indices) >= 140:
                    continue
                if w[i+d[0][0]][j+d[0][1]] == 'M' and w[i+d[1][0]][j+d[1][1]] == 'A' and w[i+d[2][0]][j+d[2][1]] == 'S' and w[i+d[3][0]][j+d[3][1]] == 'S':
                    count += 1

print(count)

