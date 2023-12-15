line = open('input.txt', 'r').read()

ans = 0


def box_index(word):
    curr = 0
    for ch in word:
        curr += ord(ch)
        curr *= 17
        curr %= 256
    return curr


boxes = {i: {} for i in range(256)}
key_list = set()
for cmd in line.split(','):
    if '=' in cmd:
        word = cmd[: cmd.index('=')]
        key_list.add(word)
        focal_length = int(cmd[cmd.index('=') + 1:])
        box_i = box_index(word)

        boxes[box_i][word] = focal_length

    if '-' in cmd:
        word = cmd[:-1]
        box_i = box_index(word)
        if word in boxes[box_i]:
            del boxes[box_i][word]

result = 0
for key in key_list:
    for box_i, value in boxes.items():
        if key in value:
            key_index = list(value).index(key)

            result += value[key] * (int(key_index) + 1) * (box_i + 1)
            break

print(boxes)
print(result)