def main():
    input = open('day9/input.txt').read().strip()
    input = [[int(x)] for x in input]

    for i in range((len(input)-1)//2):
        input[2*i].append(i)
        input[2*i + 1].append(0)
    input[len(input)-1].append((len(input)-1)//2)

    alreadyMoved = []
    newBlankSpace = 0
    idToBeMoved = 0
    sizeOfFileToBeMoved = 0

    i = len(input) - 1
    while i > 0:
        for j in range(1, i, 2):
            if input[j][0] >= input[i][0] and input[i][1] not in alreadyMoved:

                if i == len(input)-1: #if at end of list
                    idToBeMoved = input[i][1]
                    sizeOfFileToBeMoved = input[i][0]
                    input.pop(i)
                    input.pop(i-1)
                else:
                    newBlankSpace = input[i-1][0] + input[i][0] + input[i+1][0]
                    idToBeMoved = input[i][1]
                    sizeOfFileToBeMoved = input[i][0]
                    input.pop(i+1)
                    input.pop(i)
                    input.pop(i-1)
                    input.insert(i-1,[newBlankSpace,0])

                oldBlankSpace = input[j][0]
                input.pop(j)
                input.insert(j, [oldBlankSpace-sizeOfFileToBeMoved, 0])
                input.insert(j, [sizeOfFileToBeMoved, idToBeMoved])
                input.insert(j, [0,0])

                alreadyMoved.append(idToBeMoved)
                i += 2
                break
        i -= 2
    
    print(input[:50])
    print(getCheckSum(input))



    
def getCheckSum(input):
    total = 0
    count = 0
    for i in range(len(input)):
        for _ in range(input[i][0]):
            total += count*input[i][1]
            count += 1
    return total





main()
