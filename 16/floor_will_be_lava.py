from pprint import  pprint
lines = open('input.txt', 'r').read().splitlines()


def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m


def calc( x, y, dir):
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = []
    mp = {}
    # visited[0][0] = True
    queue.append((x, y, dir))
    while len(queue):
        s = queue.pop()
        curr_x, curr_y, curr_dir = s
        if (curr_x, curr_y, curr_dir) in mp:
            continue
        if is_valid(curr_x, curr_y):
            visited[curr_x][curr_y] = True
        mp[(curr_x, curr_y, curr_dir)] = True
        if curr_dir == 'left':
            curr_y = curr_y + 1
            if is_valid(curr_x, curr_y):
                if matrix[curr_x][curr_y] == '-':
                    queue.append((curr_x, curr_y, curr_dir))
                elif matrix[curr_x][curr_y] == '|':
                    queue.append((curr_x, curr_y, 'up'))
                    queue.append((curr_x, curr_y, 'down'))
                elif matrix[curr_x][curr_y] == '\\':
                    queue.append((curr_x, curr_y, 'down'))
                elif matrix[curr_x][curr_y] == '/':
                    queue.append((curr_x, curr_y, 'up'))
                else:
                    queue.append((curr_x, curr_y, curr_dir))

        if curr_dir == 'right':
            curr_y = curr_y - 1
            if is_valid(curr_x, curr_y):
                if matrix[curr_x][curr_y] == '-':
                    queue.append((curr_x, curr_y, curr_dir))
                elif matrix[curr_x][curr_y] == '|':
                    queue.append((curr_x, curr_y, 'up'))
                    queue.append((curr_x, curr_y, 'down'))
                elif matrix[curr_x][curr_y] == '\\':
                    queue.append((curr_x, curr_y, 'up'))
                elif matrix[curr_x][curr_y] == '/':
                    queue.append((curr_x, curr_y, 'down'))
                else:
                    queue.append((curr_x, curr_y, curr_dir))

        if curr_dir == 'up':
            curr_x = curr_x - 1
            if is_valid(curr_x, curr_y):
                if matrix[curr_x][curr_y] == '-':
                    queue.append((curr_x, curr_y, 'left'))
                    queue.append((curr_x, curr_y, 'right'))
                elif matrix[curr_x][curr_y] == '|':
                    queue.append((curr_x, curr_y, 'up'))
                elif matrix[curr_x][curr_y] == '\\':
                    queue.append((curr_x, curr_y, 'right'))
                elif matrix[curr_x][curr_y] == '/':
                    queue.append((curr_x, curr_y, 'left'))
                else:
                    queue.append((curr_x, curr_y, curr_dir))

        if curr_dir == 'down':
            curr_x = curr_x + 1
            if is_valid(curr_x, curr_y):
                if matrix[curr_x][curr_y] == '-':
                    queue.append((curr_x, curr_y, 'left'))
                    queue.append((curr_x, curr_y, 'right'))
                elif matrix[curr_x][curr_y] == '|':
                    queue.append((curr_x, curr_y, 'down'))
                elif matrix[curr_x][curr_y] == '\\':
                    queue.append((curr_x, curr_y, 'left'))
                elif matrix[curr_x][curr_y] == '/':
                    queue.append((curr_x, curr_y, 'right'))
                else:
                    queue.append((curr_x, curr_y, curr_dir))

    ans = 0
    for i in range(n):
        for j in range(m):
            ans += 1 if visited[i][j] else 0

    result.append(ans)


matrix = []
for line in lines:
    matrix.append([*line])

# pprint(matrix)

n = len(matrix)
m = len(matrix[0])
result = []

for i in range(n):
    calc(i, - 1, 'left')
    calc(i, m, 'right')

for i in range(m):
    calc(-1, i, 'down')
    calc(n, i, 'up')

pprint(max(result))