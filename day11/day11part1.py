def main():
    nums = [64554,35,906,6,6960985,5755,975820,0]
    for i in range(25):
        print(f'On the {i}th blink. There are {len(nums)} numbers')
        #print(nums)
        newNums = []
        for num in nums:
            if num == 0:
                newNums.append(1)
            elif len(str(num)) % 2 == 0:
                newNums.append(int(str(num)[:len(str(num))//2]))
                newNums.append(int(str(num)[len(str(num))//2:]))
            else:
                newNums.append(num*2024)
        nums = newNums
    print(len(nums))

main()