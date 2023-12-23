lines = open('input.txt', 'r').read().splitlines()


def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and matrix[x][y] != '#'


matrix = []
start_x = 0
start_y = 0
for i, line in enumerate(lines):
    matrix.append([*line])
    if 'S' in line:
        start_x = i
        start_y = line.index('S')

n = len(matrix)
m = len(matrix[0])

queue = [(start_x, start_y, 0)]

while queue:
    curr_x, curr_y, curr_i = queue.pop(0)
    if curr_i == 64:
        break
    for x, y in [(curr_x + 1, curr_y), (curr_x - 1, curr_y), (curr_x, curr_y - 1), (curr_x, curr_y + 1)]:
        if is_valid(x, y):
            if (x, y, curr_i + 1) not in queue:
                queue.append((x, y, curr_i + 1))

print(len(queue) + 1)


# print(start_x, start_y)
# print(matrix)
