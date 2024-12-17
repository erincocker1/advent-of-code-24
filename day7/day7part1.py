def main():
    input = open('day7/input.txt').read().strip().split('\n')

    total = 0
    for line in input:
        print('Currently on', line)
        testValue = int(line.split(':')[0])
        numbers = [int(x) for x in line.split(':')[1].strip().split(' ')]
        if isCorrect(numbers, testValue):
            total += testValue
    
    print(total)

        
def isCorrect(numbers, testValue):
    for i in range(2 ** (len(numbers)-1)):
        binary = format(i,'#014b')
        total = numbers[0]
        for j in range(1,len(numbers)):
            if binary[-j] == '0':
                total += numbers[j]
            else:
                total *= numbers[j]
        if total == testValue:
            return True
    return False

main()