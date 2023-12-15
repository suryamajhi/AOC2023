from pprint import pprint
lines = open('14.txt', 'r').read().splitlines()

matrix = []
for line in lines:
    matrix.append([*line])


def transpose(l1):
    l2 = list(map(list, zip(*l1)))
    return l2

matrix = transpose(matrix)
# pprint(matrix)

result = 0
for line in matrix:
    n = len(line)
    i = len(line) - 1
    count = 0
    while i >= -1:
        if line[i] == '#' or i == -1:
            first = n - i - count
            last = n - i - 1
            if i == -1:
                last = n
                first = n - count + 1
            result += count / 2 * (first + last)
            count = 0
        if line[i] == 'O':
            count += 1
        i -= 1

print(result)
