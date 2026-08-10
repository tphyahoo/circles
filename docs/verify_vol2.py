"""Every number in the Volume II do-nows, recomputed.

A chain is 66 feet and a hundred links; ten square chains make an acre.
"""
import math
import sys

ok = True


def check(claim, got, want):
    global ok
    good = got == want
    ok = ok and good
    print(f'  {"ok " if good else "NO "} {claim:58} {got}')


# ---- II.1  halfway along an odd run
check('halfway along seven links', 7 / 2, 3.5)
check('is that a whole number of links', (7 / 2).is_integer(), False)

# ---- II.2  which farm is nearer, without saying how far
A, B = (30, 40), (10, 48)
qa, qb = A[0] ** 2 + A[1] ** 2, B[0] ** 2 + B[1] ** 2
check('farm A, squares added', qa, 2500)
check('farm B, squares added', qb, 2404)
check('so B is nearer', qb < qa, True)
check('  -- but by how much? A is exactly', math.isqrt(qa), 50)
check('  -- and B is between', (math.isqrt(qb), math.isqrt(qb) + 1), (49, 50))
check('  -- so the gap is under a link, too close to eyeball', qa - qb, 96)

# ---- II.3  two diagonals, two kinds of answer
check('60 and 80: squares add to', 60 ** 2 + 80 ** 2, 10000)
check('  -- and that is a whole number squared', math.isqrt(10000) ** 2 == 10000, True)
check('50 and 50: squares add to', 50 ** 2 + 50 ** 2, 5000)
check('  -- and that one is not', math.isqrt(5000) ** 2 == 5000, False)
check('  -- it lands between', (math.isqrt(5000), math.isqrt(5000) + 1), (70, 71))

# ---- II.4  the surveyor's pocket list: whole legs under twenty, whole diagonal
triples = sorted({(a, b, math.isqrt(a * a + b * b))
                  for a in range(1, 21) for b in range(a, 21)
                  if math.isqrt(a * a + b * b) ** 2 == a * a + b * b})
print('\n  the pocket list -- both legs twenty or under:')
for a, b, c in triples:
    print(f'     {a:3} {b:3} {c:3}')
check('how many pairs work', len(triples), 7)
check('how many pairs there are altogether', 20 * 21 // 2, 210)

# ---- II.6  the stake at station 100 on a thousand-link curve
r = 1000
best = min(range(0, r + 1), key=lambda y: abs(100 ** 2 + y * y - r * r))
check('station 100, the offset that misses by least', best, 995)
check('  -- and it misses by', 100 ** 2 + 995 ** 2 - r * r, 25)
check('  -- the one below misses by', 100 ** 2 + 994 ** 2 - r * r, -1964)
check('  -- the one above misses by', 100 ** 2 + 996 ** 2 - r * r, 2016)

# ---- II.8  the round parcel, taxed by the acre
def disc(r):
    return sum(2 * math.isqrt(r * r - x * x) + 1 for x in range(-r, r + 1))


check('stakes inside a ten-chain round parcel', disc(10), 317)
check('  -- the true area, in square chains', round(math.pi * 100, 2), 314.16)
check('  -- so counting overshoots by', round(disc(10) - math.pi * 100, 2), 2.84)
check('  -- and 317 square chains is, in acres', 317 / 10, 31.7)

# ---- II.9  Pick on a five-cornered parcel
V = [(0, 0), (6, 0), (8, 3), (4, 6), (0, 4)]


def shoelace(v):
    s = sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1]
            for i in range(len(v)))
    return abs(s) / 2


def boundary(v):
    return sum(math.gcd(abs(v[(i + 1) % len(v)][0] - v[i][0]),
                        abs(v[(i + 1) % len(v)][1] - v[i][1])) for i in range(len(v)))


def inside(v):
    """Interior lattice points, by ray casting on the half-integer grid."""
    n = 0
    for x in range(0, 9):
        for y in range(0, 7):
            c, j = False, len(v) - 1
            for i in range(len(v)):
                if (v[i][1] > y) != (v[j][1] > y):
                    xc = v[i][0] + (y - v[i][1]) * (v[j][0] - v[i][0]) / (v[j][1] - v[i][1])
                    if x < xc:
                        c = not c
                j = i
            if c and not on_edge((x, y), v):
                n += 1
    return n


def on_edge(p, v):
    for i in range(len(v)):
        a, b = v[i], v[(i + 1) % len(v)]
        cross = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
        if cross == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) \
                and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]):
            return True
    return False


A5, B5, I5 = shoelace(V), boundary(V), inside(V)
check('the five-cornered parcel, area in square chains', A5, 35.0)
check('  -- stakes on the boundary', B5, 14)
check('  -- stakes strictly inside', I5, 29)
check("  -- Pick's rule: inside + boundary/2 - 1", I5 + B5 / 2 - 1, A5)
check('  -- in acres', A5 / 10, 3.5)

# ---- II.10  counting gives the area and lies about the perimeter
import sys as _s
_s.path.insert(0, '/Users/claudecode/circles/site')
import board_program

for r in (10, 100, 1000):
    n = disc(r)
    check(f'area by counting at r={r}, n/r^2', round(n / (r * r), 4),
          {10: 3.17, 100: 3.1417, 1000: 3.1415}[r])

print('\n  and the same method on the perimeter:')
for r in (12, 60, 200, 400):
    n = len(board_program.circle(r))
    print(f'     r={r:4}  {n:5} stakes   n/r = {n/r:.4f}   fence 2pi = {2*math.pi:.4f}')
# it approaches 4*sqrt(2) from just above -- the ring carries a few extra stakes
# where the column and row passes overlap, a constant that does not grow with r
gaps = [abs(len(board_program.circle(r)) / r - 4 * math.sqrt(2)) for r in (60, 200, 400)]
check('the ring count sits within 0.01 of 4*sqrt(2) at every size',
      [g < 0.01 for g in gaps], [True, True, True])
check('  -- and it is NOT approaching 2*pi',
      abs(len(board_program.circle(400)) / 400 - 2 * math.pi) > 0.6, True)
check('  -- and 2*pi is', round(2 * math.pi, 3), 6.283)
check('  -- so counting is short by, per cent',
      round(100 * (1 - 4 * math.sqrt(2) / (2 * math.pi))), 10)

print('\nVERIFIED' if ok else '\nSOMETHING IS WRONG')
sys.exit(0 if ok else 1)
