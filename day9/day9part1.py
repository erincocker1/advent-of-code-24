def main():
    input = open('day9/input.txt').read().strip()

    expandedFileData = getExpandedFileData(input)

    expandedFileData = rearrange(expandedFileData)
    print(expandedFileData[:50])
    print(expandedFileData[-50:])
    print(getCheckSum(expandedFileData))

    
def getCheckSum(expandedFileData):
    total = 0
    for i in range(len(expandedFileData)):
        total += i*expandedFileData[i]
    return total

def rearrange(expandedFileData):
    i = 0
    val = '.'
    while i < len(expandedFileData)-1:
        if expandedFileData[i] == '.':
            while True:
                val = expandedFileData.pop()
                if val != '.':
                    break
            if i >= len(expandedFileData):
                expandedFileData.append(val)
                return expandedFileData
            expandedFileData[i] = val
        i += 1
    return expandedFileData




def getExpandedFileData(input):
    expandedFileData = []
    parity = True
    id = 0
    for char in input:
        if parity:
            for i in range(int(char)):
                expandedFileData.append(id)
            id += 1
        else:
            for i in range(int(char)):
                expandedFileData.append('.')
        parity = not parity
    return expandedFileData




main()
