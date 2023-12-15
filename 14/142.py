from pprint import pprint
import json

lines = open('14.txt', 'r').read().splitlines()

matrix = []
for line in lines:
    matrix.append([*line])


def transpose(l1):
    l2 = list(map(list, zip(*l1)))
    return l2


def tilt(matrix, dir):
    new_matrix = []
    for row in matrix:
        i = 0
        count = 0
        start = 0
        stop_list = []
        while i < len(row):
            if row[i] == 'O':
                count += 1
            elif row[i] == '#':
                if count > 0:
                    stop_list.append((start, i - 1, count))
                count = 0
                start = i + 1
            i += 1
        if count > 0:
            stop_list.append((start, i - 1, count))

        for l in stop_list:
            start, stop, count = l
            tmp = ['O'] * count
            tmp1 = ['.'] * (stop - start - count + 1)
            if dir == 'east':
                row = row[:start] + tmp1 + tmp + row[stop + 1:]
            else:
                row = row[:start] + tmp + tmp1 + row[stop + 1:]
        new_matrix.append(row)
    return new_matrix


def calc(matrix):
    ans = 0
    for i, l in enumerate(matrix):
        tmp = [x for x in l if x == 'O']
        ans += len(tmp) * (len(matrix) - i)
    return ans


mp = dict()
rev_mp = dict()
mp[json.dumps(matrix)] = 0
rev_mp[0] = json.dumps(matrix)
i = 1
while i < 10000000:

    # North
    matrix = transpose(transpose(transpose(tilt(transpose(matrix), 'west'))))
    # West
    matrix = tilt(matrix, 'west')
    # South
    matrix = transpose(transpose(transpose(tilt(transpose(matrix), 'east'))))
    # East
    matrix = tilt(matrix, 'east')
    matrix_str = json.dumps(matrix)
    if matrix_str in mp:
        ex = mp[matrix_str]
        break
    else:
        mp[matrix_str] = i
        rev_mp[i] = matrix_str
    i += 1

# pprint(matrix)
# pprint(rev_mp)
# print(i, ex)

x = (1000000000 - i) % (i - ex)

print(calc(json.loads(rev_mp[x + ex])))