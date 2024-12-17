adjacents = [(-1,0),(0,1),(1,0),(0,-1)]

#count corners. equals number of sides
#check concave corners by adding coordinates of all border squares to a list. any repeats are corners
#check convex corners by looking at a plot square with multiple border squares adjacent to it

def main():
    input = [list(x) for x in open('day12/input.txt').read().strip().split('\n')]

    total = 0
    #will append a dot to indicate a square has been checked
    for i in range(140):
        for j in range(140):
            if '.' in input[i][j]:
                continue
            
            plotType = input[i][j]
            input[i][j] += '.'
            coordsInThisRegion = {(i,j): False}
            borderCoordinates = []
            sides = 0
            
            while False in coordsInThisRegion.values():
                for x in [x for x in coordsInThisRegion if coordsInThisRegion[x] == False]:
                    anyAdjacentBorderSquares = []
                    for a in adjacents:
                        locationBeingChecked = (x[0]+ a[0], x[1]+ a[1])
                        if (locationBeingChecked in coordsInThisRegion):
                            continue
                        elif locationBeingChecked[0] not in range(140) or locationBeingChecked[1] not in range(140): 
                            borderCoordinates.append(locationBeingChecked)
                            anyAdjacentBorderSquares.append(adjacents.index(a))
                        elif input[locationBeingChecked[0]][locationBeingChecked[1]] == plotType:
                            coordsInThisRegion[locationBeingChecked] = False
                            input[locationBeingChecked[0]][locationBeingChecked[1]] += '.'
                        else:
                            borderCoordinates.append(locationBeingChecked)
                            anyAdjacentBorderSquares.append(adjacents.index(a))
                    
                    sides += getNumberOfConvexCorners(anyAdjacentBorderSquares)

                    coordsInThisRegion[x] = True
            sides += getNumberOfConcaveCorners(borderCoordinates, coordsInThisRegion)
            total += sides * len(coordsInThisRegion)
            print(f'{plotType}: {sides} sides, {len(coordsInThisRegion)} area, coords: {i},{j}')

    print(total)


def getNumberOfConvexCorners(x):
    num = 0
    if (0 in x and 1 in x): num += 1
    if (1 in x and 2 in x): num += 1
    if (2 in x and 3 in x): num += 1
    if (3 in x and 0 in x): num += 1
    return num

def getNumberOfConcaveCorners(x, coordsInThisRegion):
    num = 0
    possibleCorners = []
    for item in set(x):
        if x.count(item) >= 2:
            possibleCorners.append(item)

    for item in possibleCorners:
        if all(i in coordsInThisRegion.keys() for i in [(item[0]-1, item[1]),(item[0]-1, item[1]+1),(item[0], item[1]+1)]):
            num += 1
        if all(i in coordsInThisRegion.keys() for i in [(item[0], item[1]+1),(item[0]+1, item[1]+1),(item[0]+1, item[1])]):
            num += 1
        if all(i in coordsInThisRegion.keys() for i in [(item[0]+1, item[1]),(item[0]+1, item[1]-1),(item[0], item[1]-1)]):
            num += 1
        if all(i in coordsInThisRegion.keys() for i in [(item[0], item[1]-1),(item[0]-1, item[1]-1),(item[0]-1, item[1])]):
            num += 1
    return num

main()