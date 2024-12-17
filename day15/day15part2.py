directionDict = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}

def main():
    map, directions = open('day15/input.txt').read().strip().split('\n\n')
    map = [list(row) for row in map.split('\n')]
    map = resizeMap(map) #now width 100, height still 50
    directions = ''.join(directions.split('\n'))

    for i in range(50):
        if '@' in map[i]:
            robotPos = (i, map[i].index('@'))

    for direction in directions:
        map, robotPos = moveRobot(map, robotPos, directionDict[direction])
    
    total = 0
    for i in range(50):
        for j in range(100):
            if map[i][j] == '[':
                total += (i*100) + j

    print(total)


def resizeMap(map):
    newMap = []
    for row in map:
        newRow = ''
        for x in row:
            if x == '@':
                newRow += '@.'
            elif x == '.':
                newRow += '..'
            elif x == '#':
                newRow += '##'
            elif x == 'O':
                newRow += '[]'
        newMap.append(list(newRow))
    return newMap


def moveRobot(map, robotPos, direction):
    nextPos = add(robotPos, direction)
    #free movement
    if map[nextPos[0]][nextPos[1]] == '.':
        map[robotPos[0]][robotPos[1]] = '.'
        map[nextPos[0]][nextPos[1]] = '@'
        return map, nextPos
    
    #hits a wall
    if map[nextPos[0]][nextPos[1]] == '#':
        return map, robotPos
    
    #hits a box
    if direction == (1,0) or direction == (-1,0):
        map, robotPos = moveBoxesVertically(map, robotPos, nextPos, direction)
        return map, robotPos
    if direction == (0,1) or direction == (0,-1):
        map, robotPos = moveBoxesHorizontally(map, robotPos, nextPos, direction)
        return map, robotPos

    
def moveBoxesHorizontally(map, robotPos, nextPos, direction):
    pushedPositions = []
    while map[nextPos[0]][nextPos[1]] in '[]':
        pushedPositions.append(nextPos)
        nextPos = add(nextPos, direction)
    if map[nextPos[0]][nextPos[1]] == '#':
        return map, robotPos
    
    pushedPositions.reverse()
    for pos in pushedPositions:
        map[pos[0]+direction[0]][pos[1]+direction[1]] = map[pos[0]][pos[1]]
    
    nextPos = add(robotPos, direction)
    map[nextPos[0]][nextPos[1]] = '@'
    map[robotPos[0]][robotPos[1]] = '.'
    return map, nextPos

    

def moveBoxesVertically(map, robotPos, nextPos, direction):
    pushedPositions = {nextPos} #box locations that will be pushed
    pushingPositions = {nextPos} #locations that will be pushed if they contain a box
    while True:
        newPushingPositions = set()
        for pos in pushingPositions:
            if map[pos[0]][pos[1]] == '[':
                pushedPositions.add(pos)
                pushedPositions.add((pos[0], pos[1]+1))
                newPushingPositions.add((pos[0]+direction[0], pos[1]+direction[1]))
                newPushingPositions.add((pos[0]+direction[0], pos[1]+direction[1]+1))
            elif map[pos[0]][pos[1]] == ']':
                pushedPositions.add(pos)
                pushedPositions.add((pos[0], pos[1]-1))
                newPushingPositions.add((pos[0]+direction[0], pos[1]+direction[1]))
                newPushingPositions.add((pos[0]+direction[0], pos[1]+direction[1]-1))
            elif map[pos[0]][pos[1]] == '#':
                return map, robotPos
        
        if ('[' not in [map[x[0]][x[1]] for x in pushingPositions]) and (']' not in [map[x[0]][x[1]] for x in pushingPositions]):
            break

        pushingPositions = newPushingPositions
    
    #boxes Will be pushed
    if direction == (1,0):
        pushedPositions = list(pushedPositions)
        pushedPositions.sort(key=lambda x: x[0], reverse=True)
    else:
        pushedPositions = list(pushedPositions)
        pushedPositions.sort(key=lambda x: x[0])
    
    for pos in pushedPositions:
        map[pos[0]+direction[0]][pos[1]+direction[1]] = map[pos[0]][pos[1]]
        map[pos[0]][pos[1]] = '.'
    map[nextPos[0]][nextPos[1]] = '@'
    map[robotPos[0]][robotPos[1]] = '.'

    return map, nextPos












def add(tuple1, tuple2):
    return (tuple1[0]+tuple2[0], tuple1[1]+tuple2[1])

main()