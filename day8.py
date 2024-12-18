# Day 8 of Advent of Code 2024

import collections # for part 2

# Part 1
# https://adventofcode.com/2024/day/8

# get the data
with open('input_8.txt', 'r') as f:
    data = [line.split() for line in f]

for i in range(len(data)):
    data[i] = list(data[i][0])

#  create a list for the char, a list for the tuple locations and a list of the tuple values for inflexion points

list_chars = []
list_points = []
set_inflexions = set()

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != '.':
            if data[i][j] not in list_chars:
                list_chars.append(data[i][j])
                list_points.append([(i,j)])
            else:
                list_points[list_chars.index(data[i][j])].append((i,j))

for i in range(len(list_chars)):
    for j in range(len(list_points[i])-1):
        for k in range(j+1, len(list_points[i])):
            point1 = list_points[i][j][0]
            point2 = list_points[i][k][0]
            point3 = list_points[i][j][1]
            point4 = list_points[i][k][1]
            diff_x = abs(point1 - point2)
            diff_y = abs(point3 - point4)
            if point1 > point2:
                x1 = point1 + diff_x
            elif point1 < point2:
                x1 = point1 - diff_x
            else:
                x1 = point1
            if point1 > point2:
                x2 = point2 - diff_x
            elif point1 < point2:
                x2 = point2 + diff_x
            else:
                x2 = point2

            if point3 > point4:
                y1 = point3 + diff_y
            elif point3 < point4:
                y1 = point3 - diff_y
            else:
                y1 = point3
            if point3 > point4:
                y2 = point4 - diff_y
            elif point3 < point4:
                y2 = point4 + diff_y
            else:
                y2 = point4

            if x1 >= 0 and x1 < len(data[0]) and y1 >= 0 and y1 < len(data):
                set_inflexions.add((x1, y1))
            if x2 >= 0 and x2 < len(data[0]) and y2 >= 0 and y2 < len(data):
                set_inflexions.add((x2, y2))

print('Part 1:', len(set_inflexions))

# Part 2
# https://adventofcode.com/2024/day/8

set_inflexions = set()

for i in range(len(list_chars)):
    for j in range(len(list_points[i])-1):
        for k in range(j+1, len(list_points[i])):
            pointx1 = list_points[i][j][0]
            pointx2 = list_points[i][k][0]
            pointy1 = list_points[i][j][1]
            pointy2 = list_points[i][k][1]
            diff_x = pointx1 - pointx2
            diff_y = pointy1 - pointy2

            temp_x, temp_y = pointx1, pointy1
            stopTime = False
            while not stopTime:
                temp_x = temp_x - diff_x
                temp_y = temp_y - diff_y
                if temp_x >= 0 and temp_x < len(data[0]) and temp_y >= 0 and temp_y < len(data):
                    set_inflexions.add((temp_x, temp_y))
                else:
                    stopTime = True
            
            temp_x, temp_y = pointx1, pointy1
            stopTime = False
            while not stopTime:
                temp_x = temp_x + diff_x
                temp_y = temp_y + diff_y
                if temp_x >= 0 and temp_x < len(data[0]) and temp_y >= 0 and temp_y < len(data):
                    set_inflexions.add((temp_x, temp_y))
                else:
                    stopTime = True
            
    if len(list_points[i]) > 1:
        for point in list_points[i]:
            set_inflexions.add(point)

print('Part 2:', len(set_inflexions))