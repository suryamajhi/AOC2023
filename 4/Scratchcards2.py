
result = 0
with open('1.txt', 'r') as file:
    store = []
    lines = []
    for line in file:
        store.append(1)
        lines.append(line)
        
    for i, line in enumerate(lines):
        line = line[line.index(":") + 1:]
        winner = line.split('|')[0]
        have = line.split('|')[1]
        winner_set = set([x.strip() for x in winner.split(' ')])
        have_set = set([x.strip() for x in have.split(' ')])
        winner_set.remove('')
        have_set.remove('')
        w = winner_set.intersection(have_set)
        for _ in range(store[i]):
            for j in range(len(w)):
                if i + j + 1 < len(store):
            	    store[i + j + 1] += 1
    print(sum(store))