lines = open('input.txt').read().splitlines()

result = 0
for line in lines:
    line_list = [int(x) for x in line.split(' ')]
    # line_list = line_list[::-1] Comment out of 2nd part
    last = [line_list[-1]]
    while True:
        for i, x in enumerate(line_list):
            if i == 0:
                continue
            line_list[i - 1] = x - line_list[i - 1]
        line_list = line_list[:-1]
        print(line_list)
        if line_list:
            last.append(line_list[-1])
        if not any(line_list):
            break
    print(last)
    result += sum(last)

print(result)
