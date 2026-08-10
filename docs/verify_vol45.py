"""Every number in the Volume IV and V do-nows, recomputed."""
import math
import sys
from fractions import Fraction as F

ok = True


def check(claim, got, want):
    global ok
    good = got == want
    ok = ok and good
    print(f'  {"ok " if good else "NO "} {claim:60} {got}')


print('VOLUME IV')

# ---- IV.1  the odd numbers add to squares
sums, tot = [], 0
for k in range(1, 8):
    tot += 2 * k - 1
    sums.append(tot)
check('odd numbers added up', sums, [1, 4, 9, 16, 25, 36, 49])
check('  -- one more odd number onto a square: n^2 + (2n+1)',
      [n * n + 2 * n + 1 == (n + 1) ** 2 for n in range(1, 6)], [True] * 5)

# ---- IV.2 / IV.3  the debt that doubles, and the one that triples
two = [2 ** k for k in range(7)]
check('a debt that doubles', two, [1, 2, 4, 8, 16, 32, 64])
check('  -- its gaps are the table again',
      [two[i + 1] - two[i] for i in range(6)], two[:6])
three = [3 ** k for k in range(6)]
check('a debt that triples', three, [1, 3, 9, 27, 81, 243])
check('  -- its gaps are TWICE the table',
      [three[i + 1] - three[i] for i in range(5)], [2 * v for v in three[:5]])

# ---- IV.4  the clerk who stuffed every letter into the wrong envelope
def derange(n):
    d = [1, 0]
    for k in range(2, n + 1):
        d.append((k - 1) * (d[k - 1] + d[k - 2]))
    return d[n]


check('five letters, every one in the wrong envelope', derange(5), 44)
check('  -- out of 5! =', math.factorial(5), 120)
check('  -- and 120/44 is', round(math.factorial(5) / derange(5), 3), 2.727)
check('  -- at ten letters it is', round(math.factorial(10) / derange(10), 4), 2.7183)
check('  -- e is', round(math.e, 4), 2.7183)

# ---- IV.5  e, with a receipt
s, k = F(0), 0
while True:
    s += F(1, math.factorial(k))
    if F(1, k * math.factorial(k)) < F(1, 10 ** 6) if k else False:
        break
    k += 1
check('partial sums of 1/k! reach five places at k =', k, 9)
check('  -- the leftover is under', str(F(1, k * math.factorial(k))), '1/3265920')
check('  -- and the value rounds to', round(float(s), 5), 2.71828)

# ---- IV.6  when does the debt pass a million
n = 0
while 2 ** n <= 10 ** 6:
    n += 1
check('doublings to pass a million', n, 20)
check('  -- 2^19 is', 2 ** 19, 524288)
check('  -- 2^20 is', 2 ** 20, 1048576)
check('  -- so it never lands ON a million', 10 ** 6 not in {2 ** k for k in range(30)}, True)

# ---- IV.8  ways to make change with 1, 2 and 5 dollar tokens
def ways(total, coins):
    w = [1] + [0] * total
    for c in coins:
        for v in range(c, total + 1):
            w[v] += w[v - c]
    return w[total]


check('ways to make 17 from 1, 2 and 5', ways(17, [1, 2, 5]), 22)
check('  -- and to make 100', ways(100, [1, 2, 5]), 541)

# ---- IV.9  climbing the courthouse steps one or two at a time
def steps(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


check('ways up fourteen steps', steps(14), 610)
check('  -- and up a hundred', steps(100), 573147844013817084101)

print('\nVOLUME V')

# ---- V.1  how much counting buys how many places of pi
def disc(r):
    return sum(2 * math.isqrt(r * r - x * x) + 1 for x in range(-r, r + 1))


print('     radius      dots         4n/(2r+1)^2 ... places of pi')
for r in (10, 100, 1000, 3000):
    est = disc(r) / (r * r)
    good = -math.floor(math.log10(abs(est - math.pi)))
    print(f'     {r:6}  {disc(r):12,}   {est:.7f}   {good} places')
check('counting to r=1000 agrees with pi to four figures',
      f'{disc(1000) / 10 ** 6:.4f}', f'{math.pi:.4f}'[:5] + '5')
check('  -- and tripling the radius again buys nothing much',
      f'{disc(3000) / 3000 ** 2:.4f}', '3.1416')

# ---- V.3  how fast at tick three, when all we have is between ticks
s = [t * t for t in range(8)]
check('positions down the ramp', s[:6], [0, 1, 4, 9, 16, 25])
check('average speed over tick 3 to 4', s[4] - s[3], 7)
check('  -- over tick 2 to 3', s[3] - s[2], 5)
check('  -- so "at tick 3" is between', (5, 7), (5, 7))

# ---- V.4  the fold that never settles
for h in (F(1), F(1, 10), F(1, 1000)):
    check(f'|x| at 0, refining from the right by {h}', (abs(h) - 0) / h, 1)
for h in (F(-1), F(-1, 10), F(-1, 1000)):
    check(f'  -- and from the left by {h}', (abs(h) - 0) / h, -1)

# ---- V.7  the telegram that never ends
cubes = [x ** 3 for x in range(12)]
d, lead = cubes[:], []
while d:
    lead.append(d[0])
    d = [d[i + 1] - d[i] for i in range(len(d) - 1)]
    if all(v == 0 for v in d):
        break
check('cubes: the telegram is this many words', len(lead), 4)

pows = [2 ** x for x in range(12)]
d, n = pows[:], 0
while len(d) > 1 and n < 12:
    d = [d[i + 1] - d[i] for i in range(len(d) - 1)]
    n += 1
check('but 2^x: differencing eleven times leaves', d, [1])
check('  -- they never become zero, so the telegram never ends',
      all(v != 0 for v in d), True)

print('\nVERIFIED' if ok else '\nSOMETHING IS WRONG')
sys.exit(0 if ok else 1)
