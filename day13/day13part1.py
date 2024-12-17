import re

def main():
    input = open('day13/input.txt').read().strip().split('\n\n')
    input = [x.split('\n') for x in input]

    machines = getMachinesInfo(input)

    total = 0
    for m in machines:
        if m[0][0]*m[1][1] - m[1][0]*m[0][1] == 0:
            print('AHHHHH')
            return
        a = (m[1][1]*m[2][0] - m[1][0]*m[2][1])/(m[0][0]*m[1][1] - m[1][0]*m[0][1])
        b = (m[2][0] - m[0][0]*a)/m[1][0]
        if a%1 == 0  and b%1 == 0:
            total += int(3*a + b)

    print(total)


def getMachinesInfo(input):
    machines = []
    for section in input:
        machine = []
        for line in section:
            machine.append([int(x) for x in re.findall('\d+', line)])
        machine[2][0] += 10000000000000
        machine[2][1] += 10000000000000
        machines.append(machine)
    return machines

main()

