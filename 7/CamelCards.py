from operator import itemgetter

hands = []
bid = []
mp = {}
with open('1.txt', 'r') as file:
    for line in file:
        mp[line.split(' ')[0]] = int(line.split(' ')[1])


def hand_rank(hand):
    """Return a value indicating the ranking of a hand."""
    ranks, sorted_rank = card_ranks(hand)
    if kind(5, ranks):
        return 8, ranks
    elif kind(4, ranks):
        return 7, ranks
    elif kind(3, ranks) and kind(2, ranks):
        return 6, ranks
    elif kind(3, ranks):
        return 3, ranks
    elif two_pair(sorted_rank):
        return 2, ranks
    elif kind(2, ranks):
        return 1, ranks
    else:
        return 0, ranks


def kind(n, ranks):
    """Return the first rank that this hand has extacly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None"""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return pair, lowpair
    else:
        return None

def card_ranks(cards):
    """Return a list of the ranks, sorted with higher first"""
    ranks = ['--23456789TJQKA'.index(r) for r in cards]
    sorted_rank = sorted(ranks, reverse=True)
    return ranks, sorted_rank


def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable."""
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        
    return result



hands = list(mp.keys())

# hands = ['A3Q3Q', 'A5665']
result = []
while len(hands) > 0:
    tmp = allmax(hands, key=hand_rank)[0]
    result.append(tmp)
    hands.remove(tmp)

print(result)

result.reverse()
x = 0
for i, r in enumerate(result):
    x += mp.get(r) * (i + 1)

print(x)
