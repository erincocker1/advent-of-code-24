def main():
    rules, updates = open('day5/input.txt').read().strip().split('\n\n')
    rules = [(x.split('|')[0], x.split('|')[1]) for x in rules.split('\n')]
    updates = [x.split(',') for x in updates.split('\n')]

    total = 0
    for update in updates:
        if not isCorrect(update, rules):
             orderedUpdate = putInOrder(update, rules)
             total += int(orderedUpdate[(len(update)-1)//2])

    print(total)


def isCorrect(update, rules):
    for i in range(len(update)-1):
            for j in range(i+1,len(update)):
                if (update[j],update[i]) in rules:
                    return False
    return True


def putInOrder(update, rules):
    newRules = [] #dula peep
    for rule in rules:
          if rule[0] in update and rule[1] in update:
               newRules.append(rule)
    
    newUpdate = []
    pages = update[:]
    pageThatCouldBeFirst = ''
    while len(pages) != 0:
        for page in pages:
            if couldBeFirst(page, newRules):
                pageThatCouldBeFirst = page
        newUpdate.append(pageThatCouldBeFirst)
        pages.remove(pageThatCouldBeFirst)
        newRules = [x for x in newRules if x[0] != pageThatCouldBeFirst]
  
    return newUpdate


def couldBeFirst(page, rules):
    for rule in rules:
        if rule[1] == page:
            return False
    return True
    
main()