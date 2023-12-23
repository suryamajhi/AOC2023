from pprint import pprint

lines = open('input.txt', 'r').read().splitlines()

matrix = []

for line in lines:
    matrix.append([*line])
n = len(lines)
m = len(lines[0])

start_x = 0
start_y = lines[0].index('.')

end_x = n - 1
end_y = lines[n - 1].index('.')

pprint((start_x, start_y, end_x, end_y))

stack = [(start_x, start_y, 'down', 0)]

final = []

while stack:
    curr_x, curr_y, curr_dir, curr_count = stack.pop()

    if curr_x == end_x and curr_y == end_y:
        final.append(curr_count)
        continue

    if curr_dir == 'down':
        for new_x, new_y, new_dir, no in [(curr_x + 1, curr_y, 'down', '^'), (curr_x, curr_y + 1, 'right', '<'), (curr_x, curr_y - 1, 'left','>')]:
            if matrix[new_x][new_y] != '#' and matrix[new_x][new_y] != no:
                stack.append((new_x, new_y, new_dir, curr_count + 1))

    elif curr_dir == 'up':
        for new_x, new_y, new_dir, no in [(curr_x - 1, curr_y, 'up', 'v'), (curr_x, curr_y + 1, 'right', '<'),
                                          (curr_x, curr_y - 1, 'left', '>')]:
            if matrix[new_x][new_y] != '#' and matrix[new_x][new_y] != no:
                stack.append((new_x, new_y, new_dir, curr_count + 1))

    elif curr_dir == 'right':
        for new_x, new_y, new_dir, no in [(curr_x + 1, curr_y, 'down', '^'), (curr_x - 1, curr_y, 'up', 'v'), (curr_x, curr_y + 1, 'right','<')]:
            if matrix[new_x][new_y] != '#' and matrix[new_x][new_y] != no:
                stack.append((new_x, new_y, new_dir, curr_count + 1))

    elif curr_dir == 'left':
        for new_x, new_y, new_dir, no in [(curr_x + 1, curr_y, 'down', '^'), (curr_x - 1, curr_y, 'up', 'v'), (curr_x, curr_y - 1, 'left','>')]:
            if matrix[new_x][new_y] != '#' and matrix[new_x][new_y] != no:
                stack.append((new_x, new_y, new_dir, curr_count + 1))


print(max(final))