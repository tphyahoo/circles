"""Screen illustrations — the machine register.

The projector shows machine output and only ever that: verdicts, sweeps, counts.
Precise, dark, no hand anywhere in it. The other register is board.py, which is
Mrs. Feeney's whiteboard and wobbles.
"""
import pathlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from math import isqrt, pi

BG   = '#0D1117'
BLUE = '#58A6FF'
GOLD = '#E3B341'
RED  = '#F85149'
GREY = '#8B949E'
DIM  = '#30363D'
MONO = 'monospace'

OUT = pathlib.Path(__file__).resolve().parent / 'plates'


def save(fig, name, dpi=64):
    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / name, facecolor=BG, dpi=dpi, bbox_inches='tight', pad_inches=.25)
    plt.close(fig)
    print('  wrote', OUT / name)


def style(ax, title=None):
    ax.set_facecolor(BG)
    for s in ax.spines.values():
        s.set_color(DIM)
    ax.tick_params(colors=GREY, labelsize=8)
    if title:
        ax.set_title(title, color='white', fontsize=11, family=MONO, pad=11)


# ---------------------------------------------------------------- the drawing
def mirrors(x, y):
    return {(x,y), (y,x), (-x,y), (-y,x), (x,-y), (y,-x), (-x,-y), (-y,-x)}


def walk(r, fudge=6):
    pts, x, y, d = set(), 0, r, 3 - 2*r
    while x <= y:
        pts |= mirrors(x, y)
        if d < 0:
            d += 4*x + fudge
        else:
            d += 4*(x - y) + 10; y -= 1
        x += 1
    return pts


def near_ring(p, r):
    return (2*r - 1)**2 <= 4*(p[0]**2 + p[1]**2) <= (2*r + 1)**2


def verdict(r, fudge):
    drawn = walk(r, fudge)
    if not all(near_ring(p, r) for p in drawn):        return 'Sound'
    cols = {x for (x, _) in drawn}
    if any(x not in cols for x in range(-r, r + 1)):   return 'Complete'
    if not all(mirrors(*p) <= drawn for p in drawn):   return 'Symmetric'
    return None


# ============================================== S1. the sabotage, caught at R=8
R = 8
good, bad = walk(R), walk(R, 4)
offending = sorted(p for p in bad if not near_ring(p, R))

fig, axes = plt.subplots(1, 2, figsize=(11, 5.6), facecolor=BG)
for ax, (pts, ttl) in zip(axes, [(good, 'program A'), (bad, 'program B')]):
    style(ax, ttl)
    th = [i / 300 * 6.2832 for i in range(301)]
    ax.plot([R * __import__('math').cos(t) for t in th],
            [R * __import__('math').sin(t) for t in th], color=DIM, lw=1.2, zorder=1)
    ax.scatter([p[0] for p in pts], [p[1] for p in pts], s=46, color=BLUE,
               edgecolors='none', zorder=3)
    if pts is bad:
        ax.scatter([p[0] for p in offending], [p[1] for p in offending], s=150,
                   facecolors='none', edgecolors=RED, linewidths=2.0, zorder=4)
        for (x, y) in offending[:1]:
            ax.annotate(f'({x}, {y})', (x, y), textcoords='offset points',
                        xytext=(14, -4), color=RED, fontsize=10, family=MONO)
    ax.set_xlim(-R - 1.6, R + 1.6); ax.set_ylim(-R - 1.6, R + 1.6)
    ax.set_aspect('equal')
fig.suptitle(f'R = {R}   ·   the difference is one constant, 6 against 4',
             color='white', fontsize=12.5, family=MONO, y=.97)
fig.text(.5, .012, f'{len(offending)} dots in program B lie outside what the blueprint allows — Sound is false',
         color=RED, fontsize=10, family=MONO, ha='center')
plt.tight_layout(rect=[0, .075, 1, .93])
save(fig, 's1_sabotage.png', dpi=70)


# ================================== S2. where the sabotage actually bites
radii = list(range(3, 121))
bad_v = {r: verdict(r, 4) for r in radii}
fig, ax = plt.subplots(figsize=(11, 2.9), facecolor=BG)
style(ax)
for r in radii:
    ax.bar(r, 1, width=.92, color=(RED if bad_v[r] else BLUE), edgecolor='none')
ax.set_yticks([]); ax.set_xlim(2, 121)
ax.set_xlabel('radius', color=GREY, fontsize=9, family=MONO)
ax.annotate('10', xy=(10, 1), xytext=(10, 1.9), color=GOLD, fontsize=11, family=MONO,
            ha='center', arrowprops=dict(arrowstyle='-|>', color=GOLD, lw=1.4))
ax.set_ylim(0, 2.6)
n_bad = sum(1 for r in radii if bad_v[r])
ax.set_title(f'program B, every radius from 3 to 120   ·   '
             f'wrong at {n_bad}   ·   right at {len(radii) - n_bad}',
             color='white', fontsize=11, family=MONO, pad=12)
fig.text(.5, -.06, 'blue = passes every check.  red = caught.  '
                   'ten is blue, and ten is the number on the board all lesson.',
         color=GREY, fontsize=9.5, family=MONO, ha='center')
plt.tight_layout()
save(fig, 's2_where_it_bites.png', dpi=70)


# =================================================== S3. some radii are luckier
def exact(r):
    return [(x, y) for x in range(-r, r+1) for y in range(-r, r+1) if x*x + y*y == r*r]

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.7), facecolor=BG)
for ax, r in zip(axes, (5, 25, 65)):
    style(ax, f'r = {r}   ·   {len(exact(r))} land exactly')
    ax.scatter([p[0] for p in walk(r)], [p[1] for p in walk(r)],
               s=(26 if r < 30 else 5), color=BLUE, alpha=.55, edgecolors='none')
    e = exact(r)
    ax.scatter([p[0] for p in e], [p[1] for p in e],
               s=(90 if r < 30 else 34), color=GOLD, edgecolors=BG, linewidths=.8, zorder=4)
    ax.set_xlim(-r*1.18, r*1.18); ax.set_ylim(-r*1.18, r*1.18); ax.set_aspect('equal')
fig.suptitle('gold dots sit on the ring perfectly — the whole-number triangles',
             color='white', fontsize=12.5, family=MONO, y=.98)
fig.text(.5, .012, '25 carries two different triangles, 65 carries four. '
                   'that is what makes a radius lucky.',
         color=GREY, fontsize=10, family=MONO, ha='center')
plt.tight_layout(rect=[0, .04, 1, .93])
save(fig, 's3_lucky.png', dpi=70)


# ========================================================= S4. counting to pi
def count_dots(r):
    return sum(2 * isqrt(r*r - x*x) + 1 for x in range(-r, r + 1))

rs = [3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
est = [count_dots(r) / (r * r) for r in rs]
fig, ax = plt.subplots(figsize=(9.6, 5.2), facecolor=BG)
style(ax)
ax.axhline(pi, color=GOLD, lw=1.4, ls='--', zorder=1)
ax.text(rs[-1], pi + .012, ' π', color=GOLD, fontsize=13, family=MONO, va='bottom', ha='right')
ax.plot(rs, est, color=BLUE, lw=1.6, marker='o', ms=6, zorder=3)
for r, e in [(10, est[2]), (100, est[5]), (1000, est[8])]:
    ax.annotate(f'{e:.4f}', (r, e), textcoords='offset points', xytext=(6, 10),
                color=BLUE, fontsize=9.5, family=MONO)
ax.set_xscale('log')
ax.set_xlabel('radius', color=GREY, fontsize=10, family=MONO)
ax.set_ylabel('dots inside ÷ r²', color=GREY, fontsize=10, family=MONO)
ax.set_title('count the dots, divide by the radius squared', color='white',
             fontsize=12, family=MONO, pad=12)
ax.grid(True, color=DIM, ls=':', lw=.7, alpha=.6)
plt.tight_layout()
save(fig, 's4_counting_pi.png', dpi=70)

print('\nscreen illustrations written.')


# ================================== S5. the thing that obeys every rule and is wrong
R = 25
band  = {(x, y) for x in range(-R, R+1) for y in range(-R, R+1) if near_ring((x, y), R)}
drawn = walk(R)
extra = band - drawn

fig, axes = plt.subplots(1, 2, figsize=(11, 5.7), facecolor=BG)
for ax, (pts, ttl, sub) in zip(axes, [
        (drawn, 'what we wanted', f'{len(drawn)} dots'),
        (band,  'what the rules allow', f'{len(band)} dots')]):
    style(ax, ttl)
    ax.scatter([p[0] for p in pts], [p[1] for p in pts], s=17, color=BLUE,
               edgecolors='none', zorder=3)
    if pts is band:
        ax.scatter([p[0] for p in extra], [p[1] for p in extra], s=17, color=RED,
                   edgecolors='none', zorder=4)
    ax.set_xlim(-R-2, R+2); ax.set_ylim(-R-2, R+2); ax.set_aspect('equal')
    ax.set_xlabel(sub, color=GREY, fontsize=9.5, family=MONO, labelpad=7)
fig.suptitle('both of these are Sound, Complete and Symmetric',
             color='white', fontsize=12.5, family=MONO, y=.97)
fig.text(.5, .015, 'the red dots break no rule we wrote down. at r=25 the rim reaches five dots thick.',
         color=RED, fontsize=10, family=MONO, ha='center')
plt.tight_layout(rect=[0, .06, 1, .93])
save(fig, 's5_the_band.png', dpi=70)


# ============ the three original plates, which had no generator in the repo ====
def draw_slowly(r):
    """The naive method the lesson teaches: try every dot, keep the nearest."""
    dots = set()
    for x in range(-r, r + 1):
        best = 0
        for y in range(0, r + 1):
            if abs(x*x + y*y - r*r) < abs(x*x + best*best - r*r): best = y
        dots |= {(x, best), (x, -best)}
    for y in range(-r, r + 1):
        best = 0
        for x in range(0, r + 1):
            if abs(x*x + y*y - r*r) < abs(best*best + y*y - r*r): best = x
        dots |= {(best, y), (-best, y)}
    return sorted(dots)

# p1 -- the ring at 110
r = 110; P = draw_slowly(r)
fig, ax = plt.subplots(figsize=(7, 7), facecolor=BG); style(ax, f'r = {r}   ·   {len(P)} dots')
ax.scatter([p[0] for p in P], [p[1] for p in P], s=11, color=BLUE, edgecolors='none')
ax.set_aspect('equal')
plt.tight_layout(); save(fig, 'p1_circle.png', dpi=64)

# p2 -- which dots land exactly, at 25
r = 25; P = draw_slowly(r)
E = [(x, y) for x in range(-r, r+1) for y in range(-r, r+1) if x*x + y*y == r*r]
fig, ax = plt.subplots(figsize=(7, 7), facecolor=BG)
style(ax, f'r = {r}   ·   {len(E)} dots land perfectly')
ax.scatter([p[0] for p in P], [p[1] for p in P], s=26, color=BLUE, alpha=.5,
           edgecolors='none', label=f'nearest dot ({len(P)})')
ax.scatter([p[0] for p in E], [p[1] for p in E], s=92, color=GOLD, edgecolors=BG,
           linewidths=1.2, zorder=3, label=f'lands exactly ({len(E)})')
ax.legend(facecolor='#161b22', edgecolor=DIM, labelcolor='#c9d1d9', fontsize=9, loc='upper right')
ax.set_aspect('equal')
plt.tight_layout(); save(fig, 'p2_exact.png', dpi=64)

# p3 -- the dots inside, at 10
r = 10; D = [(x, y) for x in range(-r, r+1) for y in range(-r, r+1) if x*x + y*y <= r*r]
fig, ax = plt.subplots(figsize=(7, 7), facecolor=BG)
style(ax, f'r = {r}   ·   {len(D)} dots inside   ·   {len(D)}/100 = {len(D)/100}')
ax.scatter([p[0] for p in D], [p[1] for p in D], s=30, color=BLUE, alpha=.85, edgecolors='none')
ax.set_aspect('equal')
plt.tight_layout(); save(fig, 'p3_count.png', dpi=64)
