def main():
    rules, updates = open('day5/input.txt').read().strip().split('\n\n')
    rules = [(x.split('|')[0], x.split('|')[1]) for x in rules.split('\n')]
    updates = [x.split(',') for x in updates.split('\n')]

    total = 0
    for update in updates:
        if isCorrect(update, rules):
             total += int(update[(len(update)-1)//2])
             
    
    print(total)


def isCorrect(update, rules):
    for i in range(len(update)-1):
            for j in range(i+1,len(update)):
                if (update[j],update[i]) in rules:
                    return False
    return True



main()