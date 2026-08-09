"""Every number in the chain lesson, recomputed.

The lesson claims a surveyor's chain is a counting instrument and that the
grandfather's field book is the same mathematics as the drawing. Both claims
carry numbers, so both get checked here.

A surveyor's chain is 66 feet and a hundred links, so one link is 7.92 inches.
"""
import math
import sys

import board_program

LINK_FT = 66 / 100          # a chain is 66 feet and a hundred links
ok = True


def check(claim, got, want):
    global ok
    good = got == want
    ok = ok and good
    print(f'  {"ok " if good else "NO "} {claim:58} {got}')


def exact(r):
    """Stakes that land perfectly: whole-number spots exactly r from the peg."""
    return [(x, y) for x in range(-r, r + 1)
            for y in range(-r, r + 1) if x * x + y * y == r * r]


# ---- the do now, on the board, at a size that fits
check('spots exactly 10 links from the peg', len(exact(10)), 12)
check('and one of them is the 6-8-10', (6, 8) in exact(10), True)

# ---- the same question out in the field
check('spots exactly 1000 links from the peg', len(exact(1000)), 28)
check('  -- and 600-800-1000 is among them', (600, 800) in exact(1000), True)
check('stakes the nearest rule puts there', len(board_program.circle(1000)), 5656)

# ---- what a link is worth
check('a link, in inches', round(LINK_FT * 12, 2), 7.92)
check('half a link, in inches', round(LINK_FT * 12 / 2, 2), 3.96)
check('1000 links, in feet', round(1000 * LINK_FT), 660)
check('the curve across, in feet', round(2000 * LINK_FT), 1320)

# ---- a page of the field book: offsets at every hundredth link
print('\n  the field book, radius 1000 links, a stake every hundred:')
page = []
for x in range(0, 1001, 100):
    gaps = [(abs(x * x + y * y - 1000 * 1000), y) for y in range(0, 1001)]
    best = min(gaps)[0]
    y = min(y for g, y in gaps if g == best)
    off = x * x + y * y - 1000 * 1000
    page.append((x, y, off))
    print(f'     station {x:5}   offset {y:5}   total misses by {off:+7}')

# every offset in the page must be the nearest one, and must be a whole number
for x, y, off in page:
    lo = abs(x * x + (y - 1) ** 2 - 1000 * 1000)
    hi = abs(x * x + (y + 1) ** 2 - 1000 * 1000)
    assert abs(off) <= lo and abs(off) <= hi, f'station {x} is not the nearest'
check('every offset in the page is the nearest one', True, True)

# ---- and the half-link bound, checked the integer way
worst = 0
for x, y in board_program.circle(1000):
    q4 = 4 * (x * x + y * y)
    assert (2 * 1000 - 1) ** 2 <= q4 <= (2 * 1000 + 1) ** 2, (x, y)
check('all 5656 stakes within half a link, radially', True, True)

# ---- the toy on the board and the curve in the field obey one rule
#      Least in its column OR least in its row, exactly as Circle.tla says.
#      This check was once written column-only, failed, and was relaxed to match
#      the program. That was backwards: the program was right and the module was
#      silent about rows. The module has since been corrected.
def obeys_spec(r):
    rr = r * r
    best_col = {x: min(abs(x * x + y * y - rr) for y in range(0, r + 1))
                for x in range(-r, r + 1)}
    for (x, y) in board_program.circle(r):
        gap = abs(x * x + y * y - rr)
        if gap != best_col[x] and gap != best_col[abs(y)]:
            return False
    return True


check('the board circle obeys the specification', obeys_spec(10), True)
check('so does the one in the field book', obeys_spec(1000), True)

# ---- the crossing point nobody is allowed to work out
#      station 600 on the 1000 curve: is the true offset a whole number?
check('600-800-1000 lands perfectly', 600 ** 2 + 800 ** 2 == 1000 ** 2, True)

print('\nVERIFIED' if ok else '\nSOMETHING IS WRONG')
sys.exit(0 if ok else 1)
