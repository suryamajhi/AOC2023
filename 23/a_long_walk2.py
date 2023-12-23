from pprint import pprint
import sys
sys.setrecursionlimit(20000)
lines = open('input.txt', 'r').read().splitlines()


def backtracing(curr_x, curr_y, curr_dir, curr_step):
    if curr_x == end_x and curr_y == end_y:
        if final[0] < curr_step:
            final[0] = curr_step
        return

    dir_list = []
    if curr_dir == 'down':
        dir_list = [(curr_x + 1, curr_y, 'down'), (curr_x, curr_y + 1, 'right'), (curr_x, curr_y - 1, 'left')]
    elif curr_dir == 'up':
        dir_list = [(curr_x - 1, curr_y, 'up'), (curr_x, curr_y + 1, 'right'), (curr_x, curr_y - 1, 'left')]
    elif curr_dir == 'right':
        dir_list = [(curr_x + 1, curr_y, 'down'), (curr_x - 1, curr_y, 'up'), (curr_x, curr_y + 1, 'right')]
    elif curr_dir == 'left':
        dir_list = [(curr_x + 1, curr_y, 'down'), (curr_x - 1, curr_y, 'up'), (curr_x, curr_y - 1, 'left')]

    for new_x, new_y, new_dir in dir_list:
        if matrix[new_x][new_y] != '#' and not visited[new_x][new_y]:
            visited[new_x][new_y] = True
            distance[new_x][new_y] = curr_step + 1
            backtracing(new_x, new_y, new_dir, curr_step + 1)
            visited[new_x][new_y] = False


matrix = []

for line in lines:
    matrix.append([*line])
n = len(lines)
m = len(lines[0])
print((n, m))
start_x = 0
start_y = lines[0].index('.')
end_x = n - 1
end_y = lines[n - 1].index('.')

pprint((start_x, start_y, end_x, end_y))

distance = [[0 for _ in range(m)] for _ in range(n)]
stack = [(start_x, start_y, 'down', 0)]
visited = [[False for _ in range(m)] for _ in range(n)]
final = [0]

backtracing(start_x, start_y, 'down', 0)

pprint(max(final))

# 6542 after 1.5hr :D
