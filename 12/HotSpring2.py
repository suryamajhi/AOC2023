lines = open('12.txt', 'r').read().splitlines()


# i == current position within dots
# bi == current position within blocks
# current == length of the current block of '#'


DP = {}
def f(dots, blocks, i, bi, current):
    key = (i, bi, current)
    if key in DP:
        return DP[key]
    if i == len(dots):
        if bi == len(blocks) and current == 0:
            return 1
        elif bi == len(blocks) - 1 and blocks[bi] == current:
            return 1
        else:
            return 0
    
    ans = 0
    for c in ['.', '#']:
        if dots[i] == c or dots[i] == '?':
            if c == '.' and current == 0:
                ans += f(dots, blocks, i + 1, bi, 0)
            elif c == '.' and current > 0 and bi < len(blocks) and blocks[bi] == current:
                ans += f(dots, blocks, i + 1, bi + 1, 0)
            elif c == '#':
                ans += f(dots, blocks, i + 1, bi, current + 1)

    DP[key] = ans
    return ans

ans = 0

for line in lines:
    dots, blocks = line.split()
    dots = '?'.join([dots, dots, dots, dots, dots])
    blocks = ','.join([blocks, blocks, blocks, blocks, blocks])
    blocks = [int(x) for x in blocks.split(',')]
    DP.clear()
    score = f(dots, blocks, 0, 0, 0)
    # print(dots, blocks, score)
    ans += score


print(ans)