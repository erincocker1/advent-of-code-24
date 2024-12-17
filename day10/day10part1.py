adjacents = [(-1,0),(0,-1),(0,+1),(+1,0)]


def main():
    input = [list(x) for x in open('day10/input.txt').read().strip().split('\n')]

    trailheads = getTrailheads(input)

    totalScore = 0
    for trailhead in trailheads:
        possibleRoutes = [[trailhead]] #list of lists of positions making up a possible route
        for i in range(1, 10):
            possibleRoutes = findNewPossibleRoutes(input, possibleRoutes, i)
        trailheadScore = len(set([route[-1] for route in possibleRoutes]))
        totalScore += trailheadScore

    print(totalScore)
    

def findNewPossibleRoutes(input, possibleRoutes, i):
    newPossibleRoutes = []
    for route in possibleRoutes:
        for a in adjacents:
            if route[-1][0]+a[0] not in range(48) or route[-1][1]+a[1] not in range(48):
                continue
            if input[route[-1][0]+a[0]][route[-1][1]+a[1]] == i:
                newPossibleRoutes.append(route + [(route[-1][0]+a[0],route[-1][1]+a[1])])
    return newPossibleRoutes


def getTrailheads(input):
    trailheads = []
    for i in range(48):
        for j in range(48):
            input[i][j] = int(input[i][j])
            if input[i][j] == 0:
                trailheads.append((i,j))
    return trailheads

main()
