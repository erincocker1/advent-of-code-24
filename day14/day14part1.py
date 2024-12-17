import re
L = 103
W = 101

def main():
    input = open('day14/input.txt').read().strip().split('\n')
    input = [[int(y) for y in re.findall('-?\d+', x)] for x in input]
    
    quadrants = [0,0,0,0]
    for line in input:
        newPos = ((line[0]+100*line[2]) % W, (line[1]+100*line[3]) % L)
        if newPos[0] < 50 and newPos[1] < 51:
            quadrants[0] += 1
        elif newPos[0] > 50 and newPos[1] < 51:
            quadrants[1] += 1 
        elif newPos[0] < 50 and newPos[1] > 51:
            quadrants[2] += 1 
        elif newPos[0] > 50 and newPos[1] > 51:
            quadrants[3] += 1

    print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])   

main()