"""The program on the board. This file is the single source of truth.

build_v2.py reads it and prints it into the lesson; screen.py runs it and
photographs what it prints. There is no second implementation, so the figure
cannot drift away from the code beside it.
"""


def circle(r):
    dots = set()

    # every column: try every dot, keep the best
    for x in range(-r, r + 1):
        best = 0
        for y in range(0, r + 1):
            if abs(x*x + y*y - r*r) < abs(x*x + best*best - r*r):
                best = y
        dots.add((x, best)); dots.add((x, -best))

    # then the same along the rows, for the steep sides
    for y in range(-r, r + 1):
        best = 0
        for x in range(0, r + 1):
            if abs(x*x + y*y - r*r) < abs(best*best + y*y - r*r):
                best = x
        dots.add((best, y)); dots.add((-best, y))

    return dots


def show(r):
    ring = circle(r)
    red, off = '\033[31m', '\033[0m'
    for y in range(r, -r - 1, -1):
        print(''.join(red + '. ' + off if (x, y) in ring else '. '
                      for x in range(-r, r + 1)))
