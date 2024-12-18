def getData():
    with open('input_6.txt', 'r') as f:
        return [list(line) for line in f]


def mapPrinter(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j], end='')
        print()


def findCursor(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in ['<', '>', '^', 'v']:
                return (i, j, data[i][j])


def checkOffMap(data, i, j, cursor):
    if cursor == '^':
        if i == 0:
            return True
    if cursor == '>':
        if j + 1 == len(data[0]):
            return True
    if cursor == '<':
        if j == 0:
            return True
    if cursor == 'v':
        if i + 1 == len(data):
            return True
    return False


def checkBlocked(data, i, j, cursor):
    if cursor == '^':
        if data[i-1][j] == '#':
            return True
    if cursor == '>':
        if data[i][j+1] == '#':
            return True
    if cursor == '<':
        if data[i][j-1] == '#':
            return True
    if cursor == 'v':
        if data[i+1][j] == '#':
            return True
    return False


def nextDirection(cursor):
    if cursor == '^':
        return '>'
    if cursor == '>':
        return 'v'
    if cursor == '<':
        return '^'
    if cursor == 'v':
        return '<'


def countUp(data):
    count = 0
    for line in data:
        count += line.count('X')
    print('Final Map:')
    mapPrinter(data)
    print()
    print(f'Part 1: {count}')
    quit()


def movePiece(data, i, j, cursor):
    if cursor == '^':
        return (i-1, j)
    if cursor == '>':
        return (i, j+1)
    if cursor == '<':
        return (i, j-1)
    if cursor == 'v':
        return (i+1, j)


def playGame(data, i, j, cursor):
    while True:
        data[i][j] = 'X'
        if checkOffMap(data, i, j, cursor):
            countUp(data)
        if checkBlocked(data, i, j, cursor):
            cursor = nextDirection(cursor)
        (i, j) = movePiece(data, i, j, cursor)


def main():
    data = getData()
    for line in data:
        if '\n' in line:
            line.remove('\n')

    # mapPrinter(data)

    (i, j, cursor) = findCursor(data)

    playGame(data, i, j, cursor)



if __name__ == '__main__':
    main()

# part 1 test = 41
# part 2 test = 6