"""Board illustrations — the hand register.

Mrs. Feeney's board is a whiteboard pre-printed with a faint dot lattice. The lattice is
printed: clean, precise, unemphatic. Everything drawn on it is marker: wobbly, bold, and
possibly wrong. Only marker artists get sketch params — the distinction is the point.

The other register is the projector screen: dark plates, machine output only.
"""
import pathlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as CirclePatch, Wedge

BOARD   = '#F8F7F3'
PRINTED = '#C9CDC6'
INK     = '#2E2E2C'
BLUE    = '#1B5E8C'
RED     = '#B23A2E'
HAND    = 'Marker Felt'

SKETCH = (1.0, 140, 5)      # a hand, not a seismograph


def sketchy(*artists):
    for a in artists:
        try: a.set_sketch_params(*SKETCH)
        except AttributeError: pass
    return artists[0] if len(artists) == 1 else artists


def lattice(ax, lo, hi, ms=2.6):
    for x in range(lo, hi + 1):
        for y in range(lo, hi + 1):
            ax.plot(x, y, marker='.', ms=ms, color=PRINTED, zorder=0)


def board(lo, hi, size=6.4):
    fig, ax = plt.subplots(figsize=(size, size), facecolor=BOARD)
    ax.set_facecolor(BOARD)
    lattice(ax, lo, hi)
    ax.set_xlim(lo - .7, hi + .7); ax.set_ylim(lo - .7, hi + .7)
    ax.set_aspect('equal'); ax.axis('off')
    return fig, ax



def printed_line(ax, xs, ys, lw=1.1):
    """Axes are printed on the board, so they do NOT get the marker wobble."""
    ax.plot(xs, ys, color=PRINTED, lw=lw, zorder=1, solid_capstyle='butt')


def numbers(ax, lo, hi, step=5, size=10.5):
    """Faint printed numerals along the two axes, so the dots can be named."""
    printed_line(ax, [lo, hi], [0, 0])
    printed_line(ax, [0, 0], [lo, hi])
    for v in range(lo, hi + 1):
        if v == 0 or v % step:
            continue
        ax.text(v, -.72, str(v), color=PRINTED, fontsize=size, family=HAND,
                ha='center', va='top', zorder=1)
        ax.text(-.62, v, str(v), color=PRINTED, fontsize=size, family=HAND,
                ha='right', va='center', zorder=1)
    # no label at the origin: it sits on the axis line and reads as "-0"


def local_numbers(ax, xs, ys, size=11):
    """Same idea for the zoomed figures, where every dot needs naming."""
    for v in xs:
        ax.text(v, min(ys) - .62, str(v), color=PRINTED, fontsize=size, family=HAND,
                ha='center', va='top', zorder=1)
    for v in ys:
        ax.text(min(xs) - .55, v, str(v), color=PRINTED, fontsize=size, family=HAND,
                ha='right', va='center', zorder=1)


def note(ax, x, y, s, color=INK, size=15, ha='left', va='center'):
    return ax.text(x, y, s, color=color, fontsize=size, family=HAND,
                   ha=ha, va=va, zorder=6)


def dot(ax, x, y, color=BLUE, ms=11):
    return ax.plot(x, y, 'o', ms=ms, color=color, mec=color, zorder=5)[0]


def ring(ax, r, color=INK, lw=2.0, ls='-', cx=0, cy=0, z=3):
    c = CirclePatch((cx, cy), r, fill=False, ec=color, lw=lw, ls=ls, zorder=z)
    ax.add_patch(c); sketchy(c); return c


def stroke(ax, xs, ys, color=INK, lw=2.0, ls='-', z=4, alpha=1.0):
    ln, = ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=z, alpha=alpha,
                  solid_capstyle='round')
    sketchy(ln); return ln


OUT = pathlib.Path(__file__).resolve().parent / 'plates'


def save(fig, name):
    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / name, facecolor=BOARD, dpi=100, bbox_inches='tight', pad_inches=.3)
    plt.close(fig); print('  wrote', OUT / name)


# ------------------------------------------------------------------ 1. the world
# Same -11..11 frame as figures 2, 4 and 5, so the reader can compare them --
# and so the lattice actually reaches ten, which the next line of dialogue asks for.
# The dots run to the edge of the frame rather than stopping inside it: the world
# does not have a boundary, it just leaves the picture.
fig, ax = board(-11, 11, 6.8)
numbers(ax, -11, 11)
dot(ax, 0, 0, INK, 8)
ring(ax, .75, RED, 2.2, z=5)
note(ax, 1.15, 0, 'the middle', RED, 15)
note(ax, -11.4, 12.3, 'every dot. and nothing in between them.', INK, 16)
stroke(ax, [3.03, 3.97], [4, 4], INK, 1.6)
stroke(ax, [3.03, 3.03], [3.82, 4.18], INK, 1.6)
stroke(ax, [3.97, 3.97], [3.82, 4.18], INK, 1.6)
note(ax, 3.5, 4.62, 'one unit', INK, 13, ha='center')
note(ax, -11.4, -12.4, 'it carries on past the edges of the board.', INK, 16)
save(fig, 'board_01_world.png')

# ---------------------------------------------------------- 2. Ralphie's twelve
fig, ax = board(-11, 11, 6.8)
numbers(ax, -11, 11)
for (x, y) in [(x, y) for x in range(-11, 12) for y in range(-11, 12)
               if x*x + y*y == 100]:
    dot(ax, x, y, BLUE, 10)
dot(ax, 0, 0, INK, 8)                      # the middle, so the triangle is anchored
stroke(ax, [0, 6], [0, 0], RED, 2.2)
stroke(ax, [6, 6], [0, 8], RED, 2.2)
stroke(ax, [0, 6], [0, 8], RED, 2.2)
note(ax, 3.0, -.9, '6', RED, 15, ha='center')
note(ax, 6.45, 4.0, '8', RED, 15)
note(ax, 2.15, 4.75, '10', RED, 15)
note(ax, -11.4, 12.3, 'every dot exactly ten from the middle', INK, 16)
note(ax, -11.4, -12.4, 'twelve of them. that is not a circle.', INK, 16)
save(fig, 'board_02_twelve.png')

# ------------------------------------------------------------- 3. the half-unit
# Radius 5 so the arc visibly curves; column 2, where the ring passes between the
# dots at 4 and 5. Deliberately NO decimals: working out where the ring actually
# crosses would need a square root, which is the thing this lesson refuses to take.
# The argument does not need the number -- only that the two gaps make one unit.
fig, ax = plt.subplots(figsize=(6.6, 5.6), facecolor=BOARD)
ax.set_facecolor(BOARD)
for x in range(0, 5):
    for y in range(3, 7):
        ax.plot(x, y, marker='.', ms=4.0, color=PRINTED, zorder=0)
ring(ax, 5, INK, 2.6)
local_numbers(ax, [0, 1, 2, 3, 4], [3, 4, 5, 6])
YT = 21 ** .5                       # where the ring crosses. never shown, never needed.
stroke(ax, [2, 2], [4, 5], PRINTED, 1.4, z=1)
dot(ax, 2, 5, BLUE, 13)
dot(ax, 2, 4, PRINTED, 11)
ring(ax, .30, RED, 2.2, cx=2, cy=5, z=6)

# the upper gap, in red: the one we take
stroke(ax, [2.34, 2.34], [YT, 5], RED, 2.2)
stroke(ax, [2.24, 2.44], [5, 5], RED, 1.8)
note(ax, 2.55, (YT + 5) / 2 + .04, 'this bit', RED, 13)

# the lower gap, in grey: the one we do not
stroke(ax, [2.34, 2.34], [4, YT], INK, 1.8, alpha=.5)
stroke(ax, [2.24, 2.44], [4, 4], INK, 1.6, alpha=.5)
note(ax, 2.55, (4 + YT) / 2 - .04, 'and this bit', INK, 13)

# together they are exactly one unit, and that is the whole argument
stroke(ax, [3.30, 3.30], [4, 5], INK, 1.8)
stroke(ax, [3.20, 3.40], [4, 4], INK, 1.6)
stroke(ax, [3.20, 3.40], [5, 5], INK, 1.6)
note(ax, 3.5, 4.5, 'one unit,\nbetween them', INK, 13)

note(ax, -.35, 6.6, 'column 2: the ring passes between the dots at 4 and 5', INK, 14)
note(ax, -.35, 3.28, 'the two bits make one whole unit. so whichever', INK, 14)
note(ax, -.35, 2.95, 'is shorter cannot be more than a half.', INK, 14)
ax.set_xlim(-.5, 5.1); ax.set_ylim(2.6, 6.9)
ax.set_aspect('equal'); ax.axis('off')
save(fig, 'board_03_halfdot.png')

# ------------------------------------------------ 4. nearest in every column
fig, ax = board(-11, 11, 6.8)
numbers(ax, -11, 11)
ring(ax, 10, PRINTED, 2.0, ls='--')
chosen = set()
for x in range(-10, 11):
    y = round((100 - x*x) ** .5); chosen |= {(x, y), (x, -y)}
for y in range(-10, 11):
    x = round((100 - y*y) ** .5); chosen |= {(x, y), (-x, y)}
for (x, y) in sorted(chosen):
    dot(ax, x, y, BLUE, 9)
note(ax, -11.4, 12.3, 'now take the nearest dot in every column', INK, 16)
note(ax, -11.4, -12.4, f'{len(chosen)} dots. that is a circle.', INK, 16)
save(fig, 'board_04_nearest.png')

# ----------------------------------------------------------- 5. eight mirrors
fig, ax = board(-11, 11, 6.8)
numbers(ax, -11, 11)
w = Wedge((0, 0), 11.2, 0, 45, fc=BLUE, alpha=.10, ec='none', zorder=0)
ax.add_patch(w)
for xs, ys in [([-11, 11], [0, 0]), ([0, 0], [-11, 11]),
               ([-10.6, 10.6], [-10.6, 10.6]), ([-10.6, 10.6], [10.6, -10.6])]:
    stroke(ax, xs, ys, PRINTED, 1.5, ls='--', z=1)
ring(ax, 10, PRINTED, 1.8, ls='--')
for (x, y) in {(9,4),(4,9),(-9,4),(-4,9),(9,-4),(4,-9),(-9,-4),(-4,-9)}:
    dot(ax, x, y, BLUE, 10)
dot(ax, 9, 4, RED, 13)
ring(ax, .8, RED, 2.2, cx=9, cy=4, z=6)
note(ax, 9.8, 5.3, '(9, 4)', RED, 13)
note(ax, 6.0, 1.9, 'you work out\nthis eighth', BLUE, 14, ha='center')
note(ax, -11.4, 12.3, 'the folds do the rest', INK, 16)
note(ax, -11.4, -12.4, 'one dot, worked out once, becomes eight.', INK, 16)
save(fig, 'board_05_mirrors.png')

print('\nfive board illustrations written.')

# --------------------------------------------------- 6. how you actually find it
# Column x = 7 of the radius-10 circle. Squaring turns "which is nearer" into
# arithmetic a thirteen-year-old does in their head.
fig, ax = plt.subplots(figsize=(6.6, 5.8), facecolor=BOARD)
ax.set_facecolor(BOARD)
for x in range(4, 10):
    for y in range(4, 11):
        ax.plot(x, y, marker='.', ms=3.6, color=PRINTED, zorder=0)
ring(ax, 10, INK, 2.4)
local_numbers(ax, [5,6,7,8,9], [5,6,7,8,9,10])
stroke(ax, [7, 7], [4.3, 10.3], PRINTED, 1.4, z=1)
dot(ax, 7, 7, BLUE, 13)
ring(ax, .34, RED, 2.2, cx=7, cy=7, z=6)
dot(ax, 7, 8, PRINTED, 11)
note(ax, 7.4, 8.05,  '49 + 64 = 113', INK, 14)
note(ax, 7.4, 7.62,  'thirteen too big', INK, 12)
note(ax, 7.4, 7.05,  '49 + 49 =  98', RED, 14)
note(ax, 7.4, 6.62,  'two too small  —  take it', RED, 12)
note(ax, 4.15, 10.5, 'column 7. ten away means the squares add to a hundred', INK, 14)
note(ax, 4.15, 3.95, 'so square them both and see which total', INK, 14)
note(ax, 4.15, 3.60, 'lands nearer a hundred. no ruler, no string.', INK, 14)
ax.set_xlim(4.0, 12.6); ax.set_ylim(3.25, 10.8)
ax.set_aspect('equal'); ax.axis('off')
save(fig, 'board_06_squares.png')

# ------------------------------------------------- 7. Ralphie's rule accuses
# R = 13, column 11. His rule demands the dot at 6; the drawing has 7. Working
# out which is right needs no ruler either -- just square them.
fig, ax = plt.subplots(figsize=(6.8, 5.6), facecolor=BOARD)
ax.set_facecolor(BOARD)
for x in range(8, 14):
    for y in range(3, 10):
        ax.plot(x, y, marker='.', ms=3.6, color=PRINTED, zorder=0)
ring(ax, 13, INK, 2.4)
local_numbers(ax, [9, 10, 11, 12, 13], [4, 5, 6, 7, 8, 9])
stroke(ax, [11, 11], [3.4, 9.4], PRINTED, 1.4, z=1)
dot(ax, 11, 7, BLUE, 13)
ring(ax, .34, RED, 2.2, cx=11, cy=7, z=6)
dot(ax, 11, 6, PRINTED, 11)
note(ax, 11.35, 7.05, '121 + 49 = 170', RED, 13)
note(ax, 11.35, 6.68, 'one over. take it.', RED, 12)
note(ax, 11.35, 6.05, '121 + 36 = 157', INK, 13)
note(ax, 11.35, 5.68, 'twelve under.', INK, 12)
note(ax, 8.15, 9.55, 'column 11 of the ring at 13.  169 is the target.', INK, 14)
note(ax, 8.15, 3.75, "the rule wanted the dot at 6. the drawing put", INK, 14)
note(ax, 8.15, 3.42, 'one at 7, and 7 is nearer. the rule was wrong.', INK, 14)
ax.set_xlim(8.0, 15.6); ax.set_ylim(3.0, 9.9)
ax.set_aspect('equal'); ax.axis('off')
save(fig, 'board_07_badrule.png')

# ------------------------------------------------------- 8. a lucky radius
# r = 5 by hand: twelve dots land perfectly, and they are 3-4-5 eight ways over
# plus the four on the axes.
fig, ax = board(-7, 7, 6.6)
numbers(ax, -7, 7, step=5)
ring(ax, 5, PRINTED, 1.8, ls='--')
for (x, y) in [(x, y) for x in range(-7, 8) for y in range(-7, 8) if x*x + y*y == 25]:
    dot(ax, x, y, BLUE, 12)
stroke(ax, [0, 3], [0, 0], RED, 2.2)
stroke(ax, [3, 3], [0, 4], RED, 2.2)
stroke(ax, [0, 3], [0, 4], RED, 2.2)
note(ax, 1.5, -.75, '3', RED, 14, ha='center')
note(ax, 3.35, 2.0, '4', RED, 14)
note(ax, 1.0, 2.4, '5', RED, 14)
note(ax, -7.4, 8.1, 'r = 5.  twelve dots land perfectly.', INK, 16)
note(ax, -7.4, -8.2, 'eight of them are 3-4-5 turned around.', INK, 15)
save(fig, 'board_08_lucky5.png')

# --------------------------------------------- 9. counting a column at a time
# Popovich's fix: you do not check every dot in the square, you say how tall
# each column is and add the heights up.
fig, ax = board(-11, 11, 6.8)
numbers(ax, -11, 11)
inside = [(x, y) for x in range(-10, 11) for y in range(-10, 11) if x*x + y*y <= 100]
ax.scatter([p[0] for p in inside], [p[1] for p in inside], s=26, color=BLUE,
           alpha=.30, edgecolors='none', zorder=3)
for x, col in [(-6, 8), (0, 10), (5, 8), (9, 4)]:
    h = max(y for (px, y) in inside if px == x)
    ax.scatter([x]*(2*h+1), list(range(-h, h+1)), s=30, color=BLUE,
               edgecolors='none', zorder=5)
    stroke(ax, [x + .42, x + .42], [-h, h], RED, 1.8)
    note(ax, x + .62, 0, str(2*h + 1), RED, 13)
ring(ax, 10, PRINTED, 1.8, ls='--')
note(ax, -11.4, 12.3, 'do not check every dot. measure each column.', INK, 16)
note(ax, -11.4, -12.4, 'add the heights up. that is the whole count.', INK, 16)
save(fig, 'board_09_columns.png')
