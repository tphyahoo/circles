"""Every table and count that goes into the Volume I do-nows."""
import math
import sys

ok = True


def check(claim, got, want):
    global ok
    good = got == want
    ok = ok and good
    print(f'  {"ok " if good else "NO "} {claim:56} {got}')


# I.2  the decimal that loses something
check('0.333 * 3, to three places', round(0.333 * 3, 3), 0.999)

# I.3  the sequence whose gaps give it away
seq = [n * n + 1 for n in range(1, 7)]
gaps = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
check('the table', seq, [2, 5, 10, 17, 26, 37])
check('its gaps', gaps, [3, 5, 7, 9, 11])
check('so the next entry is', seq[-1] + 13, 50)

# I.5  Galileo, 1638
s = [t * t for t in range(6)]
d1 = [s[i + 1] - s[i] for i in range(5)]
d2 = [d1[i + 1] - d1[i] for i in range(4)]
check('positions down the ramp', s, [0, 1, 4, 9, 16, 25])
check('gaps -- the odd numbers', d1, [1, 3, 5, 7, 9])
check('gaps of the gaps', d2, [2, 2, 2, 2])

# I.6  paths across a grid, right and down only
check('paths across a 3x3 grid', math.comb(6, 3), 20)
check('paths across a 2x2 grid', math.comb(4, 2), 6)

# I.7  the total of the gaps is the last minus the first
table = [1, 4, 9, 16, 25, 36, 49, 64]
g = [table[i + 1] - table[i] for i in range(len(table) - 1)]
check('a table', table, [1, 4, 9, 16, 25, 36, 49, 64])
check('its gaps', g, [3, 5, 7, 9, 11, 13, 15])
check('gaps added up', sum(g), 63)
check('last take away first', table[-1] - table[0], 63)

# I.6  the grid nobody can draw
check('paths across a 10x10 grid', math.comb(20, 10), 184756)
check('corners to fill in instead', (10 + 1) ** 2, 121)
check('drawing them at 10s each, in days', round(math.comb(20, 10) * 10 / 86400), 21)

# I.9  two rules, one table
by_step, prev = [], 1
for _ in range(6):
    by_step.append(prev); prev += 2
by_place = [2 * n - 1 for n in range(1, 7)]
check('add two to the one before', by_step, [1, 3, 5, 7, 9, 11])
check('double where you are, take one off', by_place, [1, 3, 5, 7, 9, 11])
check('same table, different work', by_step == by_place, True)

# I.8  the triangle where the formula and the counting disagree
V = [(0, 0), (6, 0), (0, 4)]
inside = [(x, y) for x in range(0, 7) for y in range(0, 5)
          if x > 0 and y > 0 and 4 * x + 6 * y < 24]
boundary = 6 + 4 + math.gcd(6, 4)
area = 6 * 4 / 2
check('area by the formula', area, 12.0)
check('dots strictly inside', len(inside), 7)
check('dots on the edge', boundary, 12)
check("Pick's: I + B/2 - 1", len(inside) + boundary / 2 - 1, area)

print('\nVERIFIED' if ok else '\nSOMETHING IS WRONG')
sys.exit(0 if ok else 1)
