"""Verify every claim before it goes back into the colophon.

The colophon is the page vouching for itself, so nothing goes in it that has not
been recomputed here.
"""
import math
import re
import pathlib
import sys
import html as H

sys.path.insert(0, '/Users/claudecode/circles/site')
import board_program

ok = True


def check(claim, got, want):
    global ok
    good = got == want
    ok = ok and good
    print(f'  {"ok " if good else "NO "} {claim:62} {got}')


# ---- exact solution counts
def exact(r):
    return sum(1 for x in range(-r, r + 1) for y in range(-r, r + 1)
               if x * x + y * y == r * r)


check('dots exactly on r=10', exact(10), 12)
check('dots exactly on r=25', exact(25), 20)
check('dots exactly on r=24', exact(24), 4)

# ---- the drawing at 110
d110 = board_program.circle(110)
check('dots in the drawing at r=110', len(d110), 624)

lo, hi = (2 * 110 - 1) ** 2, (2 * 110 + 1) ** 2
inside = all(lo <= 4 * (x * x + y * y) <= hi for x, y in d110)
check(f'all of them have 4(x^2+y^2) within {lo}..{hi}', inside, True)


# ---- integer rule vs the square-root method
def by_square_root(r):
    """The same drawing, done the forbidden way: round the square root."""
    s = set()
    for x in range(-r, r + 1):
        y = round(math.sqrt(max(r * r - x * x, 0)))
        s |= {(x, y), (x, -y)}
    for y in range(-r, r + 1):
        x = round(math.sqrt(max(r * r - y * y, 0)))
        s |= {(x, y), (-x, y)}
    return s


mismatch = [r for r in range(1, 301) if board_program.circle(r) != by_square_root(r)]
check('integer rule == square-root method, radii 1..300', mismatch, [])

# ---- the program IS the specification, not merely near it
#      Circle.tla:  Circle == { p \in Dots : Least(p,1) \/ Least(p,2) }
def spec(R):
    col = {x: min(abs(x*x + y*y - R*R) for y in range(-R, R + 1))
           for x in range(-R, R + 1)}
    row = {y: min(abs(x*x + y*y - R*R) for x in range(-R, R + 1))
           for y in range(-R, R + 1)}
    return {(x, y) for x in range(-R, R + 1) for y in range(-R, R + 1)
            if abs(x*x + y*y - R*R) in (col[x], row[y])}


off = [r for r in range(1, 121) if board_program.circle(r) != spec(r)]
check('program == Circle.tla exactly, radii 1..120', off, [])

# ---- NoTies, the way TLC checks it, but at every radius at once
ties = [(r, x, y) for r in range(1, 121) for x in range(-r, r + 1)
        for y in range(-r, r + 1)
        if x*x + y*y + x*x + (y+1)*(y+1) == 2*r*r]
check('NoTies holds at every radius 1..120', ties, [])

# ---- what is actually IN each document, so the colophon only claims those
print('\nwhat each document contains:')
txt = lambda x: ' '.join(H.unescape(re.sub(r'<[^>]+>', ' ', x)).split())
for f in ('index.html', 'counting.html'):
    s = re.sub(r'data:image/png;base64,[A-Za-z0-9+/=]+', '',
               pathlib.Path('/Users/claudecode/circles/docs/' + f).read_text())
    body = txt(s[:s.index('<footer')])
    hits = [w for w in ('110', '624', '25', '24', '19', '317', '31,417', '3,141,549',
                        '314,159,053', 'JPL', 'universe', 'NoTies', 'blueprint',
                        'Gauss', 'two squares', 'perfectly')
            if re.search(re.escape(w), body, re.I)]
    print(f'   {f:16} {hits}')

print('\nALL CLAIMS VERIFIED' if ok else '\nSOMETHING IS WRONG -- do not write the colophon')
sys.exit(0 if ok else 1)
