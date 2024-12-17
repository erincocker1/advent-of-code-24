directions = [(-1,0),(0,1),(1,0),(0,-1)]

map = open('day6/input.txt').read().strip().split('\n')
map = [list(x) for x in map]

startingLocation = (0,0)
for i in range(len(map)):
    if '^' in map[i]:
        startingLocation = (i, map[i].index('^'))
        break

currentLocation = startingLocation
dirNum = 0
while True:
    nextLocation = (currentLocation[0] + directions[dirNum][0], currentLocation[1] + directions[dirNum][1])

    if not (nextLocation[0] in range(130) and nextLocation[1] in range(130)):
        break

    if nextLocation == startingLocation:
        break

    while map[nextLocation[0]][nextLocation[1]] == '#':
        dirNum = (dirNum + 1) % 4
        nextLocation = (currentLocation[0] + directions[dirNum][0], currentLocation[1] + directions[dirNum][1])
    
    map[nextLocation[0]][nextLocation[1]] = '^'
    currentLocation = nextLocation

    

count = sum([row.count('^') for row in map])
print(count)

