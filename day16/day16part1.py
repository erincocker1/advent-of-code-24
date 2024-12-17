#dijkstra's algorithm with turns as weight.
#store a list of points with their score (1000*turns + steps) and their direction when stepped to

#loop:
#check unvisited vertices adjacent to current vertex
#get score by: currentVertex score + 1 + (? 0 or 1000 or 2000 depending on direction)
#add them to the list/update their score if it's smaller
#add current vertex to visited list (and remove from scored list?)
#change current vertex to the one with the lowest score
#repeat until get to end.

def main():
    input = open('day16/input.txt').read().strip().split('\n')
    input = [list(x) for x in input] #141x141
    
    for i in range(141):
        if 'S' in input[i]:
            start = (i,input[i].index('S'))
        if 'E' in input[i]:
            end = (i,input[i].index('E'))

    score = dijkstra(input, start, end)
    print(score)

#vertex dict: coords: [score, index of direction in directions]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
listThing = [0,1,2,3,0,1,2]
turnScores = [0,1000,2000,1000]
def dijkstra(input, start, end):
    current = start
    scoredVertices = {current: [0,1]}
    visitedVertices = []
    
    while current != end:
        i = scoredVertices[current][1]
        for n in range(4):
            direction = directions[listThing[i+n]]
            nextVertexCoords = (current[0]+direction[0],current[1]+direction[1])

            if input[nextVertexCoords[0]][nextVertexCoords[1]] == '#' or nextVertexCoords in visitedVertices:
                continue

            turnScore = turnScores[n]
            score = scoredVertices[current][0] + 1 + turnScore
            if nextVertexCoords in scoredVertices.keys():
                if score < scoredVertices[nextVertexCoords][0]:
                    scoredVertices[nextVertexCoords] = [score, listThing[i+n]]
            else:
                scoredVertices[nextVertexCoords] = [score, listThing[i+n]]

        visitedVertices.append(current)
        scoredVertices.pop(current)
        current = min(scoredVertices.keys(), key=lambda x:scoredVertices[x][0])
    return scoredVertices[current][0]


main()