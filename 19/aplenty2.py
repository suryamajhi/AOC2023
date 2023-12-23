class Node:

    def __init__(self, name, x_range, m_range, a_range, s_range):
        self.name = name
        self.x_range = x_range
        self.m_range = m_range
        self.a_range = a_range
        self.s_range = s_range
        self.children = None

    def __str__(self):
        return self.name


lines = open('input.txt', 'r').read().splitlines()


mp = {}

for line in lines:
    if not line:
        continue
    if line[0] != '{':
        x = line[:line.index('{')]
        mp[x] = line[line.index('{') + 1:-1]

start_node = Node('in', (1, 4000),(1, 4000),(1, 4000),(1, 4000))
stack = [start_node]
result = 0

while len(stack):
    curr_node = stack.pop()
    if str(curr_node) == 'A' or str(curr_node) == 'R':
        if str(curr_node) == 'A':
            result += (curr_node.x_range[1] - curr_node.x_range[0] + 1) \
                      * (curr_node.a_range[1] - curr_node.a_range[0] + 1) \
                      * (curr_node.m_range[1] - curr_node.m_range[0] + 1) * \
                      (curr_node.s_range[1] - curr_node.s_range[0] + 1)
        continue
    case = mp[str(curr_node)]
    ops = case.split(',')
    curr_x = curr_node.x_range
    curr_m = curr_node.m_range
    curr_s = curr_node.s_range
    curr_a = curr_node.a_range

    for op in ops:
        if '<' in op:
            high = int(op[2:op.index(':')])
            nex = op[op.index(':') + 1:]

            if op[0] == 'x':
                stack.append(Node(nex, (curr_x[0], high - 1), curr_m, curr_a, curr_s))
                curr_x = (high, curr_x[1])
            elif op[0] == 'm':
                stack.append(Node(nex, curr_x, (curr_m[0], high - 1), curr_a, curr_s))
                curr_m = (high, curr_m[1])
            elif op[0] == 'a':
                stack.append(Node(nex, curr_x, curr_m, (curr_a[0], high - 1), curr_s))
                curr_a = (high, curr_a[1])
            else:
                stack.append(Node(nex, curr_x, curr_m, curr_a, (curr_s[0], high - 1)))
                curr_s = (high, curr_s[1])

        elif '>' in op:
            low = int(op[2:op.index(':')])
            nex = op[op.index(':') + 1:]
            if op[0] == 'x':
                stack.append(Node(nex, (low + 1, curr_x[1]), curr_m, curr_a, curr_s))
                curr_x = (curr_x[0], low)
            elif op[0] == 'm':
                stack.append(Node(nex, curr_x, (low + 1, curr_m[1]), curr_a, curr_s))
                curr_m = (curr_m[0], low)
            elif op[0] == 'a':
                stack.append(Node(nex, curr_x, curr_m, (low + 1, curr_a[1]), curr_s))
                curr_a = (curr_a[0], low)
            else:
                stack.append(Node(nex, curr_x, curr_m, curr_a, (low + 1, curr_s[1])))
                curr_s = (curr_s[0], low)

        elif 'A' in op:
            stack.append(Node(op, curr_x, curr_m, curr_a, curr_s))
        elif 'R' in op:
            ...
        else:
            stack.append(Node(op, curr_x, curr_m, curr_a, curr_s))


print(result)


