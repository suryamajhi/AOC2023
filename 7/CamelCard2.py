from operator import itemgetter

hands = []
bid = []
mp = {}
with open('1.txt', 'r') as file:
    for line in file:
        hand, bid = line.split(' ')
        mp[hand] = int(bid)


def hand_rank(hand):
    """Return a value indicating the ranking of a hand."""
    j_count = hand.count('J')
    ranks, sorted_rank, return_rank = card_ranks(hand)
    if j_count > 0:
        if kind(4, ranks):
            return 4 + j_count, return_rank
        elif kind(3, ranks):
            return 3 + j_count, return_rank
        elif two_pair(sorted_rank):
            return 3.5, return_rank
        elif kind(2, ranks):
            return 2 + j_count, return_rank
        elif kind(1, ranks):
            return 1 + j_count, return_rank
        else:
            return j_count, return_rank
    else:
        if kind(5, ranks):
            return 5, ranks
        elif kind(4, ranks):
            return 4, ranks
        elif kind(3, ranks) and kind(2, ranks):
            return 3.5, ranks
        elif kind(3, ranks):
            return 3, ranks
        elif two_pair(sorted_rank):
            return 2.5, ranks
        elif kind(2, ranks):
            return 2, ranks
        else:
            return 1, ranks

def kind(n, ranks):
    """Return the first rank that this hand has extacly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
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
    return_rank= ['-J23456789TQKA'.index(r) for r in cards]
    ranks = [x for x in return_rank if x != 1]

    sorted_rank = sorted(ranks, reverse=True)
    return ranks, sorted_rank, return_rank


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

# hands = ['T55J5', 'KTJJT']
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
