lines = open('input.txt', 'r').read().splitlines()


ops = []
mp = {}

for line in lines:
    if not line:
        continue
    if line[0] == '{':
        ops.append(line[1:-1])
    else:
        x = line[:line.index('{')]
        mp[x] = line[line.index('{') + 1:-1]

curr = mp['in']
result = 0
for op in ops:
    vals = [x.split('=') for x in op.split(',')]
    d = {}
    for k, v in vals:
        d[k] = int(v)
    curr = mp['in']
    while curr != 'A' or curr != 'R':
        inds = curr.split(',')
        break_flag = False
        for ind in inds:
            if ':' in ind:
                comp = ind[:ind.index(':')]
                if_true = ind[ind.index(':') + 1:]

                if comp[1] == '<':
                    if d[comp[0]] < int(comp[2:]):
                        case = True
                    else:
                        case = False
                elif comp[1] == '>':
                    if d[comp[0]] > int(comp[2:]):
                        case = True
                    else:
                        case = False
                if case:
                    curr = if_true
                    break
            else:
                if ind == 'A' or ind == 'R':
                    curr = ind
                    break_flag = True
                    break
                curr = mp[ind]

        if break_flag:
            break

    if curr == 'A':
        # print(op)
        result += sum(d.values())


print(result)

