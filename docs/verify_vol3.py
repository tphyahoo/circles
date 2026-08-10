"""Every number in the Volume III do-nows, recomputed.

Spread is Wildberger's: s = sin^2(theta), got from quadrances without any angle.
"""
import math
import sys

ok = True


def check(claim, got, want):
    global ok
    good = got == want
    ok = ok and good
    print(f'  {"ok " if good else "NO "} {claim:58} {got}')


# ---- III.1  two bends do not add
def spread_from_deg(d):
    return round(math.sin(math.radians(d)) ** 2, 4)


check('spread of a 30 degree bend', spread_from_deg(30), 0.25)
check('spread of two of them (60 degrees)', spread_from_deg(60), 0.75)
check('  -- but twice 0.25 is', 0.5, 0.5)
check('  -- so turning does NOT add', spread_from_deg(60) != 0.5, True)
check('three of them (90 degrees) is', spread_from_deg(90), 1.0)
check('  -- and four (120) goes back DOWN to', spread_from_deg(120), 0.75)

# ---- III.2 / III.3  the rotation rule, and staying on a ring
def turn(p, q):
    """(a,b) * (u,v) = (au - bv, av + bu) -- multiplication of Gaussian integers."""
    return (p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0])


def quad(p):
    return p[0] ** 2 + p[1] ** 2


z = (3, 4)
p = z
quads = []
for _ in range(4):
    quads.append(quad(p))
    p = turn(p, z)
check('the 3-4-5 turn applied over and over: quadrances', quads,
      [25, 625, 15625, 390625])
check('  -- every one a power of 25', all(q == 25 ** (i + 1) for i, q in enumerate(quads)),
      True)
check('  -- so every one is a perfect square', [math.isqrt(q) ** 2 == q for q in quads],
      [True] * 4)
check('and the points themselves stay whole', turn((3, 4), (3, 4)), (-7, 24))

# ---- III.5  triples to order, from the rational parametrization
def triple(m, n):
    return (m * m - n * n, 2 * m * n, m * m + n * n)


check('m=2, n=1 gives', triple(2, 1), (3, 4, 5))
check('m=3, n=2 gives', triple(3, 2), (5, 12, 13))
big = triple(40, 9)
check('m=40, n=9 gives a leg over a thousand', big, (1519, 720, 1681))
check('  -- and it is a genuine triple', big[0] ** 2 + big[1] ** 2 == big[2] ** 2, True)

# ---- (the falling-factorial chapter was binned; kept as the reason why)
#      the family is real and clean -- and no do-now could be written for it that
#      began with somebody wanting something, so it is not a chapter.
sq = lambda x: x * x
fall2 = lambda x: x * (x - 1)
check('D(x^2) is 2x+1, not 2x -- the ugliness that motivated it',
      [sq(x + 1) - sq(x) for x in range(1, 5)], [3, 5, 7, 9])
check('D(x(x-1)) is exactly 2x -- the family is genuinely clean',
      [fall2(x + 1) - fall2(x) for x in range(1, 5)], [2, 4, 6, 8])

# ---- III.9  how few numbers rebuild a whole table
# ---- III.10  how few numbers rebuild a whole table
def rebuild(first_differences, start, n):
    """Newton's series: a table from its leading differences."""
    out, row = [], list(first_differences)
    val = start
    for _ in range(n):
        out.append(val)
        val += row[0]
        for i in range(len(row) - 1):
            row[i] += row[i + 1]
    return out


table = [x ** 3 for x in range(12)]
d = table[:]
lead = []
while d:
    lead.append(d[0])
    d = [d[i + 1] - d[i] for i in range(len(d) - 1)]
    if all(v == 0 for v in d):
        break
check('a table of cubes, twelve entries', table[:6], [0, 1, 8, 27, 64, 125])
check('  -- its leading differences', lead, [0, 1, 6, 6])
check('  -- four numbers rebuild all twelve',
      rebuild(lead[1:], lead[0], 12), table)
check('  -- so the telegram is four words, not twelve', len(lead), 4)

print('\nVERIFIED' if ok else '\nSOMETHING IS WRONG')
sys.exit(0 if ok else 1)
