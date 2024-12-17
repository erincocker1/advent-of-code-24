directionDict = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}

def main():
    map, directions = open('day15/input.txt').read().strip().split('\n\n')
    map = [list(row) for row in map.split('\n')]
    directions = ''.join(directions.split('\n'))
    
    for i in range(50):
        if '@' in map[i]:
            robotPos = (i, map[i].index('@'))

    for direction in directions:
        map, robotPos = moveRobot(map, robotPos, directionDict[direction])
    
    total = 0
    for i in range(50):
        for j in range(50):
            if map[i][j] == 'O':
                total += (i*100) + j

    print(total)



def moveRobot(map, robotPos, direction):
    nextPos = add(robotPos, direction)
    if map[nextPos[0]][nextPos[1]] == '.':
        map[robotPos[0]][robotPos[1]] = '.'
        map[nextPos[0]][nextPos[1]] = '@'
        return map, nextPos
    
    if map[nextPos[0]][nextPos[1]] == '#':
        return map, robotPos
    
    while map[nextPos[0]][nextPos[1]] == 'O':
        nextPos = add(nextPos, direction)
    if map[nextPos[0]][nextPos[1]] == '#':
        return map, robotPos
    if map[nextPos[0]][nextPos[1]] == '.':
        map[nextPos[0]][nextPos[1]] = 'O'
        map[robotPos[0]][robotPos[1]] = '.'
        nextPos = add(robotPos, direction)
        map[nextPos[0]][nextPos[1]] = '@'
        return map, nextPos
    
def add(tuple1, tuple2):
    return (tuple1[0]+tuple2[0], tuple1[1]+tuple2[1])

main()