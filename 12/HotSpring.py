
lines = open('input.txt', 'r').read().splitlines()

result = 0

count = [0] * len(lines)
mp = {}

def recursivly_find(pttr, goal, i, past, final_list, built_str, pos):
    if built_str in mp:
        print('hit')
        return mp[built_str]
    if len(goal) < len(final_list):
        return
    elif goal == final_list and len(built_str) == len(pttr):
        # print(f'{built_str} {len(built_str)}')
        count[pos] += 1
        mp[built_str] = 1
        return 1
    if i >= len(pttr):
        return

    if pttr[i] == '#':
        if past == '#':
            final_list[-1] = final_list[-1] + 1
        else:
            final_list.append(1)
        x = recursivly_find(pttr, goal, i + 1, '#', [*final_list], built_str + '#', pos)
        if x:
            if built_str in mp:
                mp[built_str] += x
            else:
                mp[built_str] = x

    elif pttr[i] == '.':
        x = recursivly_find(pttr, goal, i + 1, '.', [*final_list], built_str + '.', pos)
        if x:
            if built_str in mp:
                mp[built_str] += x
            else:
                mp[built_str] = x
    else:
        if final_list == goal[:len(final_list)]:
            x = recursivly_find(pttr, goal, i + 1, '.', [*final_list], built_str + '.', pos)
            if x:
                if built_str in mp:
                    mp[built_str] += x
                else:
                    mp[built_str] = x

        if past == '#':
            final_list[-1] = final_list[-1] + 1
        else:
            final_list.append(1)
        x = recursivly_find(pttr, goal, i + 1, '#', [*final_list], built_str + '#', pos)
        if x:
            if built_str in mp:
                mp[built_str] += x
            else:
                mp[built_str] = x


for i, line in enumerate(lines):
    pttr, goal = line.split(' ')
    goal = [int(x) for x in goal.split(',')]


    if pttr[0] == '#':
        recursivly_find(pttr, goal, 1, '#', [1], '#', i)
    elif pttr[0] == '.':
        recursivly_find(pttr, goal, 1, '.', [], '.', i)
    else:
        recursivly_find(pttr, goal, 1, '#', [1], '#', i)
        recursivly_find(pttr, goal, 1, '.', [], '.', i)

print(sum(count))
