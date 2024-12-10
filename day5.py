def getData():
    with open('input_5.txt', 'r') as f:
        return [line.split() for line in f]


def checkPassed(index, rules):
    passed = True
    for i in range(len(index)):
        for rule in rules:
            if rule[0][0:2] == index[i]:
                if rule[0][3:5] in index[:i]:
                    passed = False
                    temp = index[i]
                    index.remove(index[i])
                    position = index.index(rule[0][3:5])
                    index.insert(position, temp)
                    return checkPassed(index, rules)
    if passed:
        return index
    else:
        checkPassed(index, rules)


def main():
    data = getData()
    empty = data.index([])
    
    rules = data[0:empty]
    indexes = data[empty+1:]
    brokenIndexes = []

    count = 0

    for index in indexes:
        passed = True
        index = index[0].split(',')

        for i in range(len(index)):
            for rule in rules:
                if rule[0][0:2] == index[i]:
                    if rule[0][3:5] in index[:i]:
                        if passed:
                            brokenIndexes.append(index)
                        passed = False
        if passed:
            count += int(index[len(index)//2])
    print(f'Part 1: {count}')
    goodIndexes = []

    for index in brokenIndexes:
        toAdd = checkPassed(index, rules)
        goodIndexes.append(toAdd)

    count2 = 0
    for index in goodIndexes:
        count2 += int(index[len(index)//2])
    print(f'Part 2: {count2}')


if __name__ == '__main__':
    main()


# 143 - Part 1 test
# 123 - Part 2 test