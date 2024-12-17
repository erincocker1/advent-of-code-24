from collections import defaultdict

def main():
    nums = {64554:1, 35:1, 906:1, 6:1, 6960985:1, 5755:1, 975820:1, 0:1}
    for i in range(75):
        print(f'On the {i}th blink. There are {sum(nums.values())} numbers')
        #print(nums)
        newNums = defaultdict(int)
        for num, count in nums.items():
            if num == 0:
                newNums[1] += count
            elif len(str(num)) % 2 == 0:
                newNums[int(str(num)[:len(str(num))//2])] += count
                newNums[int(str(num)[len(str(num))//2:])] += count
            else:
                newNums[num*2024] += count
        nums = newNums
    print(sum(nums.values()))

main()