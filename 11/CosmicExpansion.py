from pprint import pprint
import copy

lines = open('input.txt', 'r').read().splitlines()

matrix = []
for line in lines:
    matrix.append([*line])

def is_valid(p, q):
    return 0 <= p < n and 0 <= q < m


def two_d_to_one_d(p, q):
    return p * m + q


def one_d_to_two_d(r):
    return [r // m, r % m]

empty_row = []
empty_col = []
for i, line in enumerate(matrix):
    try:
        line.index('#')
    except ValueError:
        empty_row.append(i)

# pprint(matrix)
col_to_expand = []
for i in range(len(matrix[0])):
    empty = True
    for j in range(len(matrix)):
        ch = matrix[j][i]
        if ch == '#':
            empty = False
            break
    if empty:
        empty_col.append(i)
        col_to_expand.append(i)

print(empty_row)
print(empty_col)


n = len(matrix)
m = len(matrix[0])

points = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '#':
            points.append(two_d_to_one_d(i, j))

result = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = one_d_to_two_d(points[i])
        x2, y2 = one_d_to_two_d(points[j])
        col_cnt = 0
        for col in empty_col:
            if y1 < col < y2 or y2 < col < y1:
                col_cnt += 1
        row_cnt = 0
        for row in empty_row:
            if x1 < row < x2 or x2 < row < x1:
                row_cnt += 1
        result += abs(x1 - x2) + abs(y1 - y2) + row_cnt * (1000000 - 1) + col_cnt * (1000000 - 1)

print(result)
