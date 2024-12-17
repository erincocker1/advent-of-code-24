from collections import defaultdict
from itertools import combinations
from math import gcd

def main():
    input = open('day8/input.txt').read().strip().split('\n')
    input = [[x for x in row] for row in input]
    allAntenna = getAntennaLocations(input)

    antinodes = set()
    for locations in allAntenna.values():
        pairs = combinations(locations,2)
        for pair in pairs:
            (dx,dy) = getSmallestInterval(pair)

            count = 0
            while (pair[0][0] - count*dx in range(50)) and (pair[0][1] - count*dy in range(50)):
                antinodes.add((pair[0][0] - count*dx, pair[0][1] - count*dy))
                count += 1

            count = 1
            while (pair[0][0] + count*dx in range(50)) and (pair[0][1] + count*dy in range(50)):
                antinodes.add((pair[0][0] + count*dx, pair[0][1] + count*dy))
                count += 1

    print(len(antinodes))



def getAntennaLocations(input):
    allAntenna = defaultdict(list)
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] != '.':
                allAntenna[input[i][j]].append((i,j))
    return allAntenna


def getSmallestInterval(pair):
    dx = pair[1][0] - pair[0][0]
    dy = pair[1][1] - pair[0][1]
    return (dx/gcd(dx,dy), dy/gcd(dx,dy))
    

main()