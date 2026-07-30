"""Drawing a circle on a lattice, with the blueprint's invariants let into the code.

The predicates below are transliterated one-for-one from `Circle.tla`, and keep the
same names, so the two files can be read side by side. If you change one, change the
other -- TLC checks the spec, these check every actual run.

They are written as `assert`, which means `python3 -O` strips them out entirely. That
is the switch, rather than commenting them out: a commented-out check silently rots,
and a stripped assert is exactly zero cost.

In practice you will not need the switch. Every predicate here is O(n) in the number
of dots drawn -- the same order as the drawing itself -- because soundness is checked
dot by dot rather than by building the whole permitted set, which would be O(r^2).

Algorithm: Bresenham's circle algorithm, CACM 20(2), Feb 1977, 100-106. See Circle.tla.
"""

# ---------------------------------------------------------------- the blueprint

def quadrance(p):
    """Squared distance. No square root appears in this file."""
    return p[0] * p[0] + p[1] * p[1]


def near_ring(p, r):
    """No more than half a unit off the ring.

    |sqrt(Q) - r| <= 1/2  is the same claim as  (2r-1)^2 <= 4Q <= (2r+1)^2,
    which stays in whole numbers.
    """
    q4 = 4 * quadrance(p)
    return (2 * r - 1) ** 2 <= q4 <= (2 * r + 1) ** 2


def mirrors(p):
    x, y = p
    return {(x, y), (y, x), (-x, y), (-y, x), (x, -y), (y, -x), (-x, -y), (-y, -x)}


# ------------------------------------------------- what a drawing owes us

def sound(drawn, r):
    """Every dot it drew was permitted.

    Spec says `drawn \\subseteq Circle`; checking membership dot by dot is the
    same claim in O(n) instead of O(r^2).
    """
    return all(near_ring(p, r) for p in drawn)


def complete(drawn, r):
    """It left no column empty."""
    columns = {x for (x, _) in drawn}
    return all(x in columns for x in range(-r, r + 1))


def symmetric(drawn, r):
    """Whatever it drew, it drew all eight mirrors of."""
    return all(mirrors(p) <= drawn for p in drawn)


def correct(drawn, r):
    return sound(drawn, r) and complete(drawn, r) and symmetric(drawn, r)


# ---------------------------------------------------------------- the drawing

def draw(r):
    """Bresenham. Walks one octant and mirrors as it goes."""
    dots = set()
    x, y, d = 0, r, 3 - 2 * r
    while x <= y:
        dots |= mirrors((x, y))
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y = y - 1
        x = x + 1

    # The invariants, let in. Stripped by `python3 -O`.
    assert sound(dots, r), f"drew a dot that was not permitted, at r={r}"
    assert complete(dots, r), f"left a column empty, at r={r}"
    assert symmetric(dots, r), f"drew a dot without its mirrors, at r={r}"
    return dots


def count_dots(r):
    """How many lattice dots lie inside radius r. Whole numbers throughout."""
    from math import isqrt
    n = 0
    for x in range(-r, r + 1):
        n = n + 2 * isqrt(r * r - x * x) + 1
    return n


if __name__ == "__main__":
    # ---------------------------------------------------------------- the boundary
    # Everything above this line is integer-only, and no_floats.py enforces that.
    # Below it we divide, and we import pi, because a count is not a decimal and
    # turning one into the other is a separate act performed for human eyes. This
    # is the only place in the file where a non-integer exists, and it is here on
    # purpose. See no_floats.py, which checks the two halves separately.
    import math
    for r in (5, 13, 25, 110):
        print(f"r={r:4d}  {len(draw(r)):5d} dots on the ring")
    for r in (10, 100, 1000):
        n = count_dots(r)
        print(f"r={r:5d}  {n:10d} dots inside   n/r^2 = {n / r**2:.6f}   pi = {math.pi:.6f}")
