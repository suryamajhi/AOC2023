import re


re_ = re.compile(r'(?P<source>\S+) = \((?P<left>\S+), (?P<right>\S+)\)')


mp = {}

with open('1.txt', 'r') as file:
    for i, line in enumerate(file):
        if i == 0:
            instruction = line
        m = re_.search(line)
        if m:
            source = m.group('source')
            left = m.group('left')
            right = m.group('right')

            mp[source] = [left, right]

curr = 'AAA'
count = 0
found = False
instruction = instruction.strip()
while True:
    for i in instruction:
        print(f'{curr} {i}')
        count += 1

        if i == 'L':
            curr = mp.get(curr)[0]
        elif i == 'R':
            curr = mp.get(curr)[1]

        if curr == 'ZZZ':
            found = True
            break
    if found:
        break

print(count)
