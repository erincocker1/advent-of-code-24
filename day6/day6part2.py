directions = [(-1,0),(0,1),(1,0),(0,-1)]

def main():
    OGmap = open('day6/input.txt').read().strip().split('\n')
    OGmap = [list(x) for x in OGmap]

    startingLocation = (0,0)
    for i in range(len(OGmap)):
        if '^' in OGmap[i]:
            startingLocation = (i, OGmap[i].index('^'))
            break

    possibleLoopCount = 0
    for i in range(130):
        for j in range(130):
            if (i,j) == startingLocation:
                continue
            map = [x[:] for x in OGmap]
            map[i][j] = '#'

            if checkIfLoop(map, startingLocation):
                possibleLoopCount += 1
            print('Done loop' , i, ', ', j)
    
    print(possibleLoopCount)




def checkIfLoop(map, startingLocation):
    currentLocation = startingLocation
    dirNum = 0

    while True:
        nextLocation = (currentLocation[0] + directions[dirNum][0], currentLocation[1] + directions[dirNum][1])

        if not (nextLocation[0] in range(130) and nextLocation[1] in range(130)):
            break

        while map[nextLocation[0]][nextLocation[1]] == '#':
            dirNum = (dirNum + 1) % 4
            nextLocation = (currentLocation[0] + directions[dirNum][0], currentLocation[1] + directions[dirNum][1])

        if dirNum == 0:
            if 'N' in map[currentLocation[0]][currentLocation[1]]:
                return True
            map[currentLocation[0]][currentLocation[1]] += 'N'
        elif dirNum == 1:
            if 'E' in map[currentLocation[0]][currentLocation[1]]:
                return True
            map[currentLocation[0]][currentLocation[1]] += 'E'
        if dirNum == 2:
            if 'S' in map[currentLocation[0]][currentLocation[1]]:
                return True
            map[currentLocation[0]][currentLocation[1]] += 'S'
        if dirNum == 3:
            if 'W' in map[currentLocation[0]][currentLocation[1]]:
                return True
            map[currentLocation[0]][currentLocation[1]] += 'W'
        
        currentLocation = nextLocation
    return False

    



main()