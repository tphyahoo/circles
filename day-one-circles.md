# Circles on a Finite Grid — What Day 1 Should Have Been

*The honest version of Mrs. Feeney's lesson. Same universe, same conceit, but every
claim here has been checked against actual computation. Where a claim came out
differently than the story wanted, the claim lost.*

---

## The setup

We work on a clock with `p` ticks, `p` prime. Our numbers are `0, 1, ..., p-1`, and
counting past `p-1` wraps to `0`. A **circle** is every grid point satisfying

```
x² + y² ≡ c   (mod p)
```

That's it. No pi, no arc length, no smooth curve. Just a set of points. The interesting
question is not "what does it look like" — it's **"how many points, and what structure
do they carry?"** Both have exact, provable answers, and they're prettier than the
picture.

---

## 1. The count is exact, and `p mod 4` decides it

For any `c ≠ 0`:

| | number of points |
|---|---|
| `p ≡ 1 (mod 4)` | **`p − 1`** |
| `p ≡ 3 (mod 4)` | **`p + 1`** |

Verified for `c = 4`: p=17 → 16 points, p=19 → 20, p=101 → 100, p=103 → 104.

Note what this does **not** say. It does not say circles vanish for `p ≡ 3 (mod 4)`.
Those primes give you *one more* point, not zero. There is no "breaking point" prime.

### The one case where the circle really does collapse

Set `c = 0` and the two worlds split violently:

| | points at `c = 0` |
|---|---|
| `p ≡ 1 (mod 4)` | `2p − 1` — **two crossed lines** through the origin (33 at p=17) |
| `p ≡ 3 (mod 4)` | `1` — **the origin, alone** |

*This* is where `p mod 4` earns its reputation. Try `p=17, c=0` against `p=19, c=0`.

---

## 2. Why — and this is the good part

Remember the two square roots of `−1`? They're not a side quest. **They are the reason
the count is what it is.**

**When `p ≡ 1 (mod 4)`,** a genuine `i` lives on the clock — a real grid number with
`i² = −1`. At p=17 it's `4`, since `4² = 16 = −1`. And the moment you have it, the
circle equation *factors*:

```
x² + y²  =  (x + iy)(x − iy)
```

Verified: this holds at every one of the `p²` grid points, for p = 13, 17, 29.

So substitute `u = x + iy`, `v = x − iy`. The equation becomes just `u·v = c`. Now count:
pick `u` to be any of the `p−1` nonzero values, and `v = c/u` is forced. **`p − 1`
solutions.** The count isn't a coincidence to memorize — it falls out of the factoring.

**When `p ≡ 3 (mod 4)`,** no such `i` exists on the clock. So you build one: adjoin `i`
and get a new, larger field of size `p²`. In it, `x² + y²` is the *norm* of `x + iy`, and
the norm map is `(p²−1)/(p−1) = p+1`-to-one onto the nonzero values. **`p + 1`
solutions.**

> **The correction that matters most.** Day 1 claimed we don't need imaginary units.
> That's exactly backwards. For half of all primes you must adjoin `i`, and the thing
> you get — `F_p[i]`, of size `p²` — is the finite mirror of the complex numbers. The
> ultrafinite universe does not escape `C`. It builds a scale model of it.

---

## 3. The circle is a rotation group — for real, not by analogy

Here's what should have been the headline. Define, for two points on the circle `x²+y²=1`:

```
(a, b) ⋆ (u, v)  =  (au − bv,  av + bu)
```

That's complex multiplication, written without complex numbers. **The circle is closed
under it** — verified exhaustively for p = 7, 11, 13, 17, 19, 29, 31. Multiply any two
points on the circle and you land on the circle. It's a group.

Better: **the group is cyclic.** There's a single point that, multiplied by itself over
and over, visits *every other point on the circle exactly once* before returning home.

| p | circle size | a generator |
|---|---|---|
| 7 | 8 | (2, 2) |
| 13 | 12 | (2, 6) |
| 17 | 16 | (4, 6) |
| 19 | 20 | (3, 7) |
| 29 | 28 | (5, 11) |
| 103 | 104 | (2, 10) |

So a finite circle *does* have rotation — a smallest turn, `1/(p∓1)` of the way around,
that generates all the others. This is the honest version of the rotation lesson, and
it's better than the one told: not "here's a trick for 90°," but **"the circle is
literally the group of rotations, and it's cyclic, and here's a generator."**

Ask yourself: is the generator's orbit in *visual* circular order as it steps around?
(It isn't. Chasing why is a great problem.)

---

## 4. What genuinely has no analogue

Being straight about the losses, because the original lesson wasn't:

- **No distance.** `F_p` has no ordering — you can't ask whether one point is farther
  than another. "Radius" is a label on an equation, not a length.
- **No angle, no arc, no pi.** Not "we cleverly avoided pi." There is no arc to measure.
  Pi's absence is a *missing feature*, not a victory over infinity.
- **No betweenness.** No point lies between two others, so the circle isn't a curve.
- **What survives:** the count, the group, the symmetry, the factoring. That's a lot!
  It's just algebra rather than geometry.

---

## 5. The picture is the *least* interesting part — and it gets worse with size

The story promised that at ~10,000 ticks the dots blur into a smooth ring. **The opposite
is true.** The points equidistribute: roughly `p` of them scattered over `p²` cells, so
density falls like `1/p`. At p=65537 the plot is uniform dust with no ring at all.

Structure lives at **small** `p`:

| p, c | fraction on one ring |
|---|---|
| 17, 7 | **100%** |
| 29, 3 | 86% (24 of 28 — the best-looking one) |
| 53, 49 | 62% |
| 109, 92 | 44% |

Searched every residue of every prime below 600; past ~150 nothing beat about 40%.

**Why any ring appears at all:** a clean arc shows up where `x² + y²` equals `c + kp` as a
*genuine integer* with no wraparound. So the modular circle is a stack of real integer
circles, and one dominates when `c + kp` happens to have many representations as a sum
of two squares. For `p=29, c=3` that integer is `650 = 2·5²·13`, with 24 representations.
Since the total is always about `p` and the ring grows far slower, big clean circles
simply do not exist.

---

## 6. The example that undercut the whole premise

Day 1 opened on: *no fraction squares to 2, so we use a modular grid to find the exact
number that does.*

But whether `√2` exists mod `p` depends on `p mod 8` — it exists exactly when
`p ≡ ±1 (mod 8)`:

| p | 5 | 7 | 13 | 17 | 23 | 29 | 31 | 41 |
|---|---|---|---|---|---|---|---|---|
| `√2` exists? | no | yes | no | yes | yes | no | yes | yes |

Three of the four clocks taught that day — 5, 13, 29 — **cannot solve the equation the
lesson was built to solve.** The fix is the same as before: extend to `F_p²`. Which is,
again, the move the story claimed to have made unnecessary.

---

## The one-paragraph version

A circle mod `p` has exactly `p−1` points when `p ≡ 1 (mod 4)` and `p+1` when
`p ≡ 3 (mod 4)`, and the reason is that `x²+y²` factors as `(x+iy)(x−iy)` precisely when
`−1` is a square — so the two roots of `x² = −1` *are* the theorem. Those points form a
cyclic group under complex multiplication, so the circle genuinely is a rotation group
with a smallest turn. What you give up is metric geometry: no distance, no angle, no pi,
and no smooth curve ever, at any size — the points equidistribute, so large primes look
like noise and the prettiest pictures are the small ones.

---

### Corrections to the original lesson

| Claimed | Actually |
|---|---|
| Primes ≡ 3 mod 4 make the circle "entirely disappear" | They give `p+1` points — *more* than ≡ 1 mod 4 |
| ~10,000 ticks blurs into a smooth unbroken ring | Equidistributes into uniform dust; structure is at small `p` |
| p=257 organizes into bands like a classic circle | Mostly scatter, one small genuine ring near centre |
| A 13-clock circle has exactly 18 points | Impossible — a 13-clock yields only 12 or 25 |
| We never need imaginary units | For `p ≡ 3 mod 4` you must adjoin `i`; `F_p[i]` is finite `C` |
| We find the exact grid number squaring to 2 | Only when `p ≡ ±1 (mod 8)`; fails on 5, 13, 29 |
| Ultrafinitism won a medieval war ("Great Limit Wars") | Invented. Real ultrafinitism is a live minority position |
