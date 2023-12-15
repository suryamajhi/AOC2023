line = open('input.txt', 'r').read()

ans = 0
for l in line.split(','):
    curr = 0
    for ch in l:
        curr += ord(ch)
        curr *= 17
        curr %= 256
    ans += curr

print(ans)