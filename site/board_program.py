"""The program on the board. This file is the single source of truth.

build_v2.py reads it and prints it into the lesson; photograph.py runs it and
captures what it prints. There is no second implementation, so the figure cannot
drift away from the code beside it.

circle() follows Circle.tla exactly.
"""


def circle(r):
    dots = set()

    # every column: which dot's total misses r*r by least?
    for x in range(-r, r + 1):
        gaps = [(abs(x*x + y*y - r*r), y) for y in range(0, r + 1)]
        best = min(gap for gap, _ in gaps)
        for gap, y in gaps:
            if gap == best:
                dots.add((x, y)); dots.add((x, -y))

    # then the same along the rows, for the steep sides
    for y in range(-r, r + 1):
        gaps = [(abs(x*x + y*y - r*r), x) for x in range(0, r + 1)]
        best = min(gap for gap, _ in gaps)
        for gap, x in gaps:
            if gap == best:
                dots.add((x, y)); dots.add((-x, y))

    return dots


def show(r):
    ring = circle(r)
    red, off = '\033[31m', '\033[0m'
    for y in range(r, -r - 1, -1):
        print(''.join(red + '. ' + off if (x, y) in ring else '. '
                      for x in range(-r, r + 1)))
