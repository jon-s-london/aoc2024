def getData():
    with open('input_4.txt', 'r') as f:
        return [list(line) for line in f]


def checkDirection(direction, i, j, data, length, depth):
    minMaxi = i + direction[0] * 3
    minMaxj = j + direction[1] * 3
    if minMaxj < 0 or minMaxj > length:
        return False
    if minMaxi < 0 or minMaxi > depth:
        return False
    if data[i+direction[0]][j+direction[1]] == 'M' and data[i+direction[0]*2][j+direction[1]*2] == 'A' and data[i+direction[0]*3][j+direction[1]*3] == 'S':
        # print(f'got one where i={i} and j={j}')
        return True


def searchForXmas(data,i,j,length, depth):
    searchable = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    count = 0
    for direction in searchable:
        if checkDirection(direction, i, j, data, length, depth):
            count += 1
    return count


def xmas(data, length, depth):
    count = 0

    for i in range(depth + 1):
        for j in range(length - 1):
            if data[i][j] == 'X':
                count += searchForXmas(data, i, j, length, depth)
    return count


def searchForCrossMas(data, i, j, length, depth):
    searchable = [(-1,-1), (1,1), (-1,1), (1,-1)]

    if data[i-1][j-1] == 'M' and data[i-1][j+1] == 'M' and data[i+1][j+1] == 'S' and data[i+1][j-1] == 'S':
        return 1
    elif data[i-1][j-1] == 'S' and data[i-1][j+1] == 'S' and data[i+1][j+1] == 'M' and data[i+1][j-1] == 'M':
        return 1
    elif data[i-1][j-1] == 'S' and data[i+1][j-1] == 'S' and data[i-1][j+1] == 'M' and data[i+1][j+1] == 'M':
        return 1
    elif data[i-1][j-1] == 'M' and data[i+1][j-1] == 'M' and data[i-1][j+1] == 'S' and data[i+1][j+1] == 'S':
        return 1
    else:
        return 0


def crossMas(data, length, depth):
    count = 0

    for i in range(1, depth):
        for j in range(1, length - 2):
            if data[i][j] == 'A':
                count += searchForCrossMas(data, i, j, length, depth)
    return count

def main():
    data = getData()
    length = len(data[0])
    depth = len(data) - 1

    count = xmas(data, length, depth)
    print(f'Part 1: {count}')

    count2 = crossMas(data, length, depth)
    print(f'Part 2: {count2}')


if __name__ == '__main__':
    main()
