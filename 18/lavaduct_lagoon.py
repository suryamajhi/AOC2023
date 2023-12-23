lines = open('input.txt', 'r').read().splitlines()


def is_inside(points, xp, yp):
    cnt = 0
    for i in range(1, len(points)):
        [x1, y1] = points[i - 1]
        [x2, y2] = points[i]
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp-y1)/(y2-y1))*(x2-x1):
            cnt += 1
    return cnt%2 == 1


curr = (0, 0)
edges = []
max_x = 0
max_y = 0
min_x = 0
min_y = 0
for line in lines:
    x, y = curr
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    d, count, color = line.split(' ')
    if d == 'R':
        [edges.append((x, y + i)) for i in range(int(count))]
        curr = (x, y + int(count))
    if d == 'L':
        [edges.append((x, y - i)) for i in range(int(count))]
        curr = (x, y - int(count))
    if d == 'U':
        [edges.append((x - i, y)) for i in range(int(count))]
        curr = (x - int(count), y)
    if d == 'D':
        [edges.append((x + i, y)) for i in range(int(count))]
        curr = (x + int(count), y)


inside = 0
for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        if (i, j) in edges:
            continue
        if is_inside(edges, i, j):
            inside += 1


print(len(edges) + inside)
