lines = open('input.txt').read().splitlines()

matrix = []
for i, line in enumerate(lines):
    matrix.append([*line])
    if 'S' in line:
        start_x = i
        start_y = line.index('S')

n = len(matrix)
m = len(matrix[0])


def is_inside(points, xp, yp):
    cnt = 0
    for i in range(1, len(points)):
        [x1, y1] = points[i - 1]
        [x2, y2] = points[i]
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp-y1)/(y2-y1))*(x2-x1):
            cnt += 1
    return cnt%2 == 1


def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m


def insert_into_queue(x, y, old_x, old_y, validators):
    if not is_valid(x, y) or (matrix[x][y] not in validators) or matrix[x][y] == '.' or matrix[x][y] == 'S':
        return
    if visited[x][y]:
        if distance[x][y] + distance[old_x][old_y] + 1 >= result[0]:
            result[0] = distance[x][y] + distance[old_x][old_y] + 1
            p = point_vector[x][y][::-1]
            p.extend(point_vector[old_x][old_y])
            point_vector[x][y] = p
            final.append(x)
            final.append(y)
        return
    visited[x][y] = True
    distance[x][y] = distance[old_x][old_y] + 1
    point_vector[x][y].extend(point_vector[old_x][old_y])
    queue.append([x, y, old_x, old_y])


visited = [[False for _ in range(m)] for _ in range(n)]
distance = [[0 for _ in range(m)] for _ in range(n)]
point_vector = [[[i * m + j] for j in range(m)] for i in range(n)]

result = [0]
queue = []
visited[start_x][start_y] = True

final = []

insert_into_queue(start_x - 1, start_y, start_x, start_y, ['|', 'F', '7'])
insert_into_queue(start_x, start_y - 1, start_x, start_y, ['-', 'F', 'L'])
insert_into_queue(start_x, start_y + 1, start_x, start_y, ['-', 'J', '7'])
insert_into_queue(start_x + 1, start_y, start_x, start_y, ['|', 'J', 'L'])


# print(matrix)

while len(queue):
    curr = queue.pop(0)
    curr_x = curr[0]
    curr_y = curr[1]
    old_x = curr[2]
    old_y = curr[3]
    ch = matrix[curr_x][curr_y]

    if ch == '|':
        if curr_x > old_x:
            insert_into_queue(curr_x + 1, curr_y, curr_x, curr_y, ['|', '7', 'F', 'J', 'L'])
        else:
            insert_into_queue(curr_x - 1, curr_y, curr_x, curr_y, ['|', '7', 'F', 'J', 'L'])

    if ch == '-':
        if curr_y > old_y:
            insert_into_queue(curr_x, curr_y + 1, curr_x, curr_y, ['-', '7', 'F', 'J', 'L'])
        else:
            insert_into_queue(curr_x, curr_y - 1, curr_x, curr_y, ['-', '7', 'F', 'J', 'L'])

    if ch == 'L':
        if curr_x > old_x:
            insert_into_queue(curr_x, curr_y + 1, curr_x, curr_y, ['-', '7', 'F', 'J', '|'])
        else:
            insert_into_queue(curr_x - 1, curr_y, curr_x, curr_y, ['-', '7', 'F', 'J', '|'])

    if ch == 'J':
        if curr_x > old_x:
            insert_into_queue(curr_x, curr_y - 1, curr_x, curr_y, ['-', '7', 'F', 'L', '|'])
        else:
            insert_into_queue(curr_x - 1, curr_y, curr_x, curr_y, ['-', '7', 'F', 'L', '|'])

    if ch == '7':
        if curr_x < old_x:
            insert_into_queue(curr_x, curr_y - 1, curr_x, curr_y, ['-', 'J', 'F', 'L', '|'])
        else:
            insert_into_queue(curr_x + 1, curr_y, curr_x, curr_y, ['-', 'J', 'F', 'L', '|'])

    if ch == 'F':
        if curr_x < old_x:
            insert_into_queue(curr_x, curr_y + 1, curr_x, curr_y, ['-', 'J', '7', 'L', '|'])
        else:
            insert_into_queue(curr_x + 1, curr_y, curr_x, curr_y, ['-', 'J', '7', 'L', '|'])

# print(final)
points = [[i // m, i % m] for i in point_vector[final[0]][final[1]]]

count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if not [i, j] in points:
            if is_inside(points, i, j):
                count += 1

# print(points)
print(count)
print(result[0] // 2)