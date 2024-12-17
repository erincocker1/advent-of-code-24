from collections import defaultdict
from itertools import combinations

def main():
    input = open('day8/input.txt').read().strip().split('\n')
    input = [[x for x in row] for row in input]
    allAntenna = getAntennaLocations(input)

    antinodes = []
    for locations in allAntenna.values():
        pairs = combinations(locations,2)
        for pair in pairs:
            antinodes = checkIsNewAntinode(2*pair[0][0] - pair[1][0], 2*pair[0][1] - pair[1][1], antinodes)
            antinodes = checkIsNewAntinode(2*pair[1][0] - pair[0][0], 2*pair[1][1] - pair[0][1], antinodes)

    print(len(antinodes))


def getAntennaLocations(input):
    allAntenna = defaultdict(list)
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] != '.':
                allAntenna[input[i][j]].append((i,j))
    return allAntenna

def checkIsNewAntinode(i,j, antinodes):
    if ((i,j) not in antinodes) and i in range(50) and j in range(50):
        antinodes.append((i,j))
    return antinodes
    

main()