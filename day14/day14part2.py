import re
import matplotlib.pyplot as plt
L = 103
W = 101


#103j -101i = 49
def main():
    vals = [101*i + 97 for i in range(1000)]
    otherVals = [103*i + 48 for i in range(1000)]
    intersections = set(vals) & set(otherVals)
    print(intersections)

    input = open('day14/input.txt').read().strip().split('\n')
    input = [[int(y) for y in re.findall('-?\d+', x)] for x in input]
    #49 is weird??
    for i in range(0,91000):
        for line in input:
            line[0] = (line[0]+line[2]) % W
            line[1] = (line[1]+line[3]) % L
        
        if i in intersections:
            plt.scatter([line[0] for line in input], [-line[1] for line in input])
            plt.title(f'{i+1} seconds')
            plt.savefig(str(i+1) + 'secs.png')
            plt.clf()


#101(i+1) - 3, 101i +98
#and 103(i+1) - 54, 103i +49
#49, 98, 152, 199, 300, 401, 502, 603, 704

main()