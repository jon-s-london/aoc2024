# Day 1 of Advent of Code 2024

# Part 1
# https://adventofcode.com/2024/day/1

# get the data
with open('input_1.txt', 'r') as f:
    data = [line.split() for line in f]

# create 2 lists for each set of data and a total for the sum
listA = []
listB = []
total = 0

# loop the data and split into 2 lists
for i in range(len(data)):
    listA.append(int(data[i][0]))
    listB.append(int(data[i][1]))

# sort the lists, sort will make it in numerical order
listA.sort()
listB.sort()

# loop through the lists and get the difference
for i in range(len(listA)):
    total += abs(listA[i] - listB[i])

# print the total
print('Total for Part 1:', total)

# Part 2
# https://adventofcode.com/2024/day/1#part2

# setup a new total for the multiplication in part 2
part2Total = 0

# loop through the lists
# count of item in list B * item value in list A
for i in range(len(listA)):
    part2Total += listB.count(listA[i]) * listA[i]

# print the total
print('Total for Part 2:', part2Total)
