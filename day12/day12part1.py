adjacents = [(-1,0),(0,1),(1,0),(0,-1)]

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
            perimeter = 0
            while False in coordsInThisRegion.values():
                for x in [x for x in coordsInThisRegion if coordsInThisRegion[x] == False]:
                    for a in adjacents:
                        locationBeingChecked = (x[0]+ a[0], x[1]+ a[1])
                        if (locationBeingChecked in coordsInThisRegion):
                            continue
                        elif locationBeingChecked[0] not in range(140) or locationBeingChecked[1] not in range(140): 
                            perimeter += 1
                        elif input[locationBeingChecked[0]][locationBeingChecked[1]] == plotType:
                            coordsInThisRegion[locationBeingChecked] = False
                            input[locationBeingChecked[0]][locationBeingChecked[1]] += '.'
                        else:
                            perimeter += 1
                    coordsInThisRegion[x] = True
            total += len(coordsInThisRegion) * perimeter

    print(total)

main()