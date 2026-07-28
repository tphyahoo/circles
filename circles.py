import matplotlib.pyplot as plt
import numpy as np

def generate_ultrafinite_circle(p, r_squared):
    """
    Finds all discrete pixel coordinates (x, y) that satisfy 
    the circle equation: x^2 + y^2 = r_squared (mod p)
    """
    # Bucket every y by its square, so we can look up "what has square s?" in O(1).
    # This is what keeps big primes tractable -- scanning the full p x p grid would
    # be 4.3 billion steps at p = 65537, versus 65537 here.
    roots_of = {}
    for y in range(p):
        roots_of.setdefault(y * y % p, []).append(y)

    x_points = []
    y_points = []

    # For each x, the equation pins y^2 exactly -- just fetch its roots
    for x in range(p):
        for y in roots_of.get((r_squared - x * x) % p, ()):
            x_points.append(x)
            y_points.append(y)

    return np.array(x_points), np.array(y_points)

def plot_modular_grid(p, r_squared):
    # Residues only run 0..p-1, so anything larger would silently match nothing
    r_squared %= p

    # Generate the constellation of points
    x, y = generate_ultrafinite_circle(p, r_squared)
    
    # Setup the digital lab display
    plt.figure(figsize=(8, 8), facecolor='#0d1117')
    ax = plt.gca()
    ax.set_facecolor('#0d1117')
    
    # Shrink the stars as the grid grows, or big primes render as one solid blob.
    # Outlines only help while the markers are large enough to have an inside.
    dot_size = min(30, max(0.5, 4000 / p))
    edges = '#1f6feb' if dot_size > 4 else 'none'

    # Plot the grid points as glowing galaxy stars
    plt.scatter(x, y, color='#58a6ff', s=dot_size, alpha=0.8, edgecolors=edges, label=f'Discrete Points ({len(x)})')
    
    # Configure grid lines to match our finite field boundaries
    plt.xlim(-0.5, p - 0.5)
    plt.ylim(-0.5, p - 0.5)
    plt.xticks(np.arange(0, p, max(1, p // 10)))
    plt.yticks(np.arange(0, p, max(1, p // 10)))
    
    # Style the axes
    ax.tick_params(colors='white', grid_color='#21262d')
    ax.spines['bottom'].set_color('#30363d')
    ax.spines['left'].set_color('#30363d')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend(facecolor='#161b22', edgecolor='#30363d', labelcolor='#c9d1d9')
    # mathtext has no \pmod, so spell the modulus out longhand
    plt.title("Ultrafinite Circle Constellation\n"
              rf"$x^2 + y^2 \equiv {r_squared} \ (\mathrm{{mod}}\ {p})$",
              color='white', fontsize=14, pad=15)
    plt.xlabel("X Coordinate (Modular Clock Ticks)", color='#8b949e', labelpad=10)
    plt.ylabel("Y Coordinate (Modular Clock Ticks)", color='#8b949e', labelpad=10)
    
    plt.show()

# ==========================================
# EXPERIMENT LAB: Tweak these parameters!
# ==========================================
# Try p = 17, p = 101, or p = 257. Any odd prime works -- for a nonzero radius you
# get p - 1 points when p % 4 == 1, and p + 1 points when p % 4 == 3.
#
# Where p % 4 really matters is RADIUS_SQUARED = 0. For p % 4 == 1 the circle
# degenerates into two crossed lines (33 points at p = 17); for p % 4 == 3 all you
# get is the origin. Worth flipping between p = 17 and p = 19 to see it.
#
# SHOWCASE -- pairs that actually look like a circle, found by scoring every
# residue of every prime below 600 on "what fraction of points share one radius":
#
#     (p, r^2)   ring    on ring   radius
#     (17,  7)   100%    16        5.7     perfect, but sparse
#     (17,  3)   100%    16        7.9     perfect, but sparse
#     (29,  3)    86%    24       12.7     the sweet spot -- reads as a circle
#     (53, 49)    62%    32       23.5     bigger ring, noise creeping in
#     (109, 92)   44%    48       52.6     rim still visible through the scatter
#
# The tradeoff is structural, not a tuning problem. A clean ring appears where
# x^2 + y^2 equals c + k*p as a genuine integer with no wraparound, so the ring's
# size is the number of ways to write that integer as a sum of two squares -- which
# grows far slower than p. Hence ~p total points, a ring that barely grows, and
# large primes that dissolve into dust. Above ~150 nothing beats about 40%.
#
# ------------------------------------------------------------------
# THINGS TO ACTUALLY TRY  (replaces the suggestions this script shipped
# with, which described results the code does not produce)
# ------------------------------------------------------------------
# 1. THE CIRCLE THAT DOESN'T COLLAPSE.  Run (17, 4), then (19, 4). The original
#    notes promised primes like 7, 11, 19 make the circle "entirely disappear."
#    They don't -- you get MORE points, not fewer: 16 at p=17, 20 at p=19.
#
# 2. THE ONE THAT REALLY DOES COLLAPSE.  Set RADIUS_SQUARED = 0 and compare
#    p = 17 against p = 19. That is where p % 4 bites: 33 points forming two
#    crossed lines, versus a single lonely point at the origin.
#
# 3. BEST CIRCLE IN THE BOOK.  (29, 3) -- 24 of 28 points on one ring.
#    (17, 7) and (17, 3) are mathematically perfect at 100%, just sparse.
#
# 4. WATCH IT DISSOLVE, NOT RESOLVE.  Run 29, then 109, then 257, then 65537.
#    The original notes claimed ~10,000 ticks blurs into a smooth unbroken ring.
#    The opposite happens: the points are equidistributed, so big primes look
#    like uniform dust. Structure lives at SMALL p.
#
# 5. OPEN QUESTION.  At p = 17 the ring fraction jumps around by radius --
#    50%, 75%, 100% -- and it is not explained by whether r^2 is a square
#    mod p (3 and 7 are non-squares and hit 100%; 5 and 11 are non-squares
#    and sit at 50%). Something else decides it. Worth digging into.
CLOCK_SIZE_P = 29
RADIUS_SQUARED = 3

plot_modular_grid(CLOCK_SIZE_P, RADIUS_SQUARED)
