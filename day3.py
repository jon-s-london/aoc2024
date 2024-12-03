def getData():
    with open('input_3.txt', 'r') as f:
        return [line for line in f]


def isThreeNumbers(data, i):
    numbers = ['0', '1','2','3','4','5','6','7','8','9']
    if data[0][i+4] in numbers:
        if data[0][i+5] in numbers:
            if data[0][i+6] in numbers:
                return 3
            return 2
        return 1
    else:
        return 0


def part1(data):
    sum = 0
    count = 0
    for i in range(len(data[0]) - 8):
        if data[0][i:i+4] == 'mul(':
            firstNumberLength = isThreeNumbers(data, i)
            if firstNumberLength in [1,2,3]:
                if data[0][i+4+firstNumberLength:i+4+firstNumberLength+1] ==',':
                    secondNumberLength = isThreeNumbers(data, i+firstNumberLength+1)
                    if secondNumberLength in [1,2,3]:
                        if data[0][i+4+firstNumberLength+1+secondNumberLength:i+4+firstNumberLength+1+secondNumberLength+1] ==')':
                            # do the calculation
                            sum += int(data[0][i+4:i+4+firstNumberLength]) * int(data[0][i+4+firstNumberLength+1:i+4+firstNumberLength+secondNumberLength+1])
                            # print(sum)
                            count += 1
    return sum


def part2(data):
    isDo = True
    sum = 0
    print(data[0][0:3])
    for i in range(len(data[0]) - 8):
        if data[0][i:i+4] == 'do()':
            isDo = True
            print(data[0][i:i+4])
        elif data[0][i:i+7] == "don't()":
            isDo = False
            print(data[0][i:i+7])
        if data[0][i:i+4] == 'mul(':
            firstNumberLength = isThreeNumbers(data, i)
            if firstNumberLength in [1,2,3]:
                if data[0][i+4+firstNumberLength:i+4+firstNumberLength+1] ==',':
                    secondNumberLength = isThreeNumbers(data, i+firstNumberLength+1)
                    if secondNumberLength in [1,2,3]:
                        if data[0][i+4+firstNumberLength+1+secondNumberLength:i+4+firstNumberLength+1+secondNumberLength+1] ==')':
                            # do the calculation
                            if isDo:
                                sum += int(data[0][i+4:i+4+firstNumberLength]) * int(data[0][i+4+firstNumberLength+1:i+4+firstNumberLength+secondNumberLength+1])
    return sum


if __name__ == "__main__":
    # get the data
    data = getData()
    data2 = [data[0] + data[1] + data[2] + data[3] + data[4] + data[5]]
    first = part1(data2)
    print('First Part:', first)
    second = part2(data2)
    print('Second Part:', second)

# mul(4,4) is 8 digits long