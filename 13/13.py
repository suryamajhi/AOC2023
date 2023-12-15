from pprint import pprint


lines = open('input.txt', 'r').read().splitlines()

groups = []
group = []
for line in lines:
    if not line:
        groups.append(group)
        group = []
        continue
    group.append(line)

groups.append(group)

# pprint(groups)


def calculate(group, type):
    for i in range(0, len(group) - 1):
        j = i
        k = j + 1
        while j >= 0 and k < len(group):
            if group[j] == group[k]:
                j -= 1
                k += 1
            else:
                break
        if k >= len(group) or j < 0:
            return (i + 1) * type
    return 0


def transpose(l1):
    l2 = list(map(list, zip(*l1)))
    return l2


result = 0
for group in groups:
    result += calculate(group, 100)   # Row
    result += calculate(transpose(group), 1)   # Col
    
print(result)

