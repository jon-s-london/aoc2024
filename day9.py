# Day 9 of Advent of Code 2024

def part1():
    # Part 1
    # https://adventofcode.com/2024/day/9

    # get the data
    with open('input_9.txt', 'r') as f:
        data = [line.split() for line in f]

    drive = []

    for i in range(len(data[0][0])):

        if i % 2 == 0:
            for j in range(int(data[0][0][i])):
                drive.append(i//2)
        else:
            for j in range(int(data[0][0][i])):
                drive.append('.')


    isWorking = True

    while isWorking:
        nextDot = drive.index('.')

        # traverse drive backwards
        for i in range(len(drive)-1, -1, -1):
            if i < nextDot:
                isWorking = False
                break
            elif drive[i] != '.':
                drive[nextDot] = drive[i]
                drive[i] = '.'
                break

    sum = 0

    for i in range(len(drive)):
        if drive[i] != '.':
            sum += i * int(drive[i])

    print('Part 1:', sum)


def part2():
    # Part 2
    # https://adventofcode.com/2024/day/9

    # get the data
    with open('input_9_test.txt', 'r') as f:
        data = [line.split() for line in f]

    drive = ''

    for i in range(len(data[0][0])):

        if i % 2 == 0:
            for j in range(int(data[0][0][i])):
                drive = drive + str(i//2)
        else:
            for j in range(int(data[0][0][i])):
                drive = drive + '.'

    isWorking = True

    while isWorking:
        counter = 0
        count = 0

        # traverse drive backwards
        for i in range(len(drive)-1, -1, -1):
            if drive[i] != '.':
                if drive[i-1] == drive[i]:
                    count += 1
                else:
                    tempString = '.'
                    tempChars = drive[i]
                    for j in range(count):
                        tempString = tempString + '.'
                        tempChars = drive[i] + tempChars
                    space = drive.index(tempString)
                    driveTemp = drive[0:space] + tempChars + drive[space+len(tempString):i] + tempString + drive[len(tempString) + len(tempChars):]
                    drive = driveTemp
                    count = 0

            else:
                count = 0
        
        counter += 1
        if counter > 100:
            isWorking = False


if __name__ == '__main__':
    # part1()
    part2()