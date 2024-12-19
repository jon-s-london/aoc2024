# Day 10 of Advent of Code 2024


def checkNeighbours(data, i, j, num):
    if i-1 > 0:
        if data[i-1][j] == num+1:
            checkNeighbours(data, i-1, j, num)
    if i+1 < len(data):
    
    if j-1 > 0:
    
    if j+1 < len(data[i]):


def part1():
    # Part 1
    # https://adventofcode.com/2024/day/10

    # get the data
    with open('input_10_test.txt', 'r') as f:
        data = [line.split() for line in f]
    
    for i in range(len(data)):
        data[i] = list(data[i][0])

    print(data)

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '0':
                checkNeighbours(data, i, j, '0')


if  __name__ == '__main__':
    part1()
