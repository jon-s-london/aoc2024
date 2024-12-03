# Day 2 of Advent of Code 2024

# https://adventofcode.com/2024/day/2


def lineChecker(line):
    i = 1
    if int(line[i-1]) < int(line[i]):
        isUp = True # ascending line
    elif int(line[i-1]) > int(line[i]):
        isUp = False # descending line
    else:
        return False # 2 numbers equal - fails
    while i < len(line):
        before, current = int(line[i-1]), int(line[i])
        if abs(before - current) not in [1, 2, 3]:
            return False # goes up or down too much
        if (isUp and before > current) or (not isUp and before < current):
            return False # going the wrong way for this step
        i += 1
    return True


def lineChecker2(line):
    # check as is whether it passes and return True
    if lineChecker(line):
        return True
    # else pop each individual part and check again and return True

    for i in range(len(line)):
        newLine = line.copy()
        newLine.pop(i)
        if lineChecker(newLine):
            return True
    return False


def getData():
    with open('input_2.txt', 'r') as f:
        return [line.split() for line in f]


def part1(data):
    count = 0
    for line in data:
        if lineChecker(line):
            count += 1
    print('Part 1:', count)


def part2(data):
    count = 0
    for line in data:
        if lineChecker2(line):
            count += 1
    print('Part 2:', count)


if __name__ == "__main__":
    # get the data
    data = getData()
    part1(data)
    part2(data)
