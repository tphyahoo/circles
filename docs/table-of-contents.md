# A Finite Route Through School Mathematics

**Draft table of contents.** Seventh grade through single-variable calculus, with a
gesture beyond. Set against the traditional sequence so the divergences are visible.

Nothing here is new mathematics. Sources are credited per volume; the point is the
*order*, not the content.

### A standing debt

The nearest existing book is **Graham, Knuth & Patashnik, *Concrete Mathematics* (1989)**,
and this outline should say so on its first page rather than in a footnote. Volumes I,
III, V and VII are all walking through territory it mapped: the difference operator,
falling factorials, telescoping, summation by parts, generating functions, recurrences.
Read it before writing a word of this.

It also supplies this project's best evidence. *Concrete Mathematics* exists because
Stanford computer science students who had completed calculus could not handle sums and
recurrences, and needed six hundred pages of remediation to get there. That is a
measurement, taken in our world, of the gap this book proposes to close from the other
side — and it is a stronger argument for the book than any claim about whether infinity
is real.

The difference between the two projects is audience and order. *Concrete Mathematics* is
for people who already have the calculus and need the discrete half; this is for people
who have neither, taking the discrete half first.

---

## What it is for

The substrate is **computation**. Not as a career and not as a subject beside the
others, but as the tool the rest of it is done with — the way arithmetic is the
substrate now.

A graduate specialises afterward, into statistics or physics or algebraic geometry
or building software, and arrives at any of them able to say what a procedure does
before running it, in notation that cannot be read two ways. Very few people in our
world get that at all; the ones who do get it at thirty, at work, badly.

The trade is real and should be stated rather than discovered. **They do not come
out knowing the physics and statistics an honors student here does.** Our sequence
surveys everything and delivers mastery of nothing in particular; this one picks one
thing and delivers it. A reader who wants the survey should buy the survey.

The standing debt above is also the best evidence for the trade. *Concrete
Mathematics* is six hundred pages of remediation, sold to people who already have
the degree, for precisely the gap this proposes to close from the other side.

**What this is not.** It is not "teach kids to code," which every school system has
now attempted, and which produces students who can write a hundred lines of
JavaScript and cannot say what any of it does. The distinction is
computation-as-mathematics against coding-as-vocation, and it is worth restating
because the failure mode is one short hop away: the moment the subject becomes the
apparatus — how to specify, how to make it fast, what a tool is *for* — the
mathematics has stopped moving. Legibility is the whole of what the formal notation
is here to buy. Nothing beyond that is in scope.

---

## How this differs, structurally

Four differences do all the work. Everything else follows from them.

**1. Organized by operation, not by object.** The traditional sequence is a tour of
kinds of thing — integers, then linear functions, then quadratics, then polynomials,
then exponentials, then trigonometric functions. This one is a tour of three verbs:
**count**, **difference**, **sum**. The objects arrive as answers to questions about
the verbs. Quadratics aren't a unit; they're *what has a constant second difference*.

**2. Calculus starts in seventh grade.** The difference operator `Δ` is subtracting
adjacent entries in a table. A twelve-year-old can do it on day one. So Volume I
contains the Fundamental Theorem of Calculus — as telescoping, which is a one-line
proof. The traditional sequence defers the same idea by five years because it insists
on limits first.

**3. Sequences are the primary object; functions are secondary.** A function is a table
of values. Traditional books treat sequences as a late Algebra II sidebar, which is
backwards: the table is the thing you can actually hold.

**4. The hard part moves to the end, and shrinks.** Limits and convergence traditionally
gate everything, arriving early and blocking the door. Here they arrive last and only
matter for the cases where refinement genuinely fails — because everything before them
*terminated*.

Two consequences worth flagging: square roots and `π` are late and derived rather than
early and given, and induction — the finitist's proof engine — does the heavy lifting
from Volume I onward instead of appearing once in Algebra II.

What is *unchanged*: order of operations, solving equations, fractions, coordinates,
factoring. The elementary layer is already finite. Nobody needs saving from it.

---

## Volume I — Seventh Grade: Counting Things

*Traditional: ratios and proportions · negative numbers · expressions and equations ·
area, surface area, volume · sampling and probability*

1. Numbers You Can Point At
2. Exact Fractions — why a fraction is a pair of whole numbers, and never a decimal
3. Tables, and the Gaps Between Their Entries — `Δ` introduced
4. When the Gap Never Changes — linear, discovered rather than defined
5. When the Gap's Gap Never Changes — quadratics, before the quadratic formula
6. Pascal's Triangle Is a Machine
7. Sums That Collapse — `Σ` as the undoing of `Δ`; the Fundamental Theorem, unnamed
8. Dots in a Box — area by counting

> *Credits:* Boole (1860) and Jordan (1939) for the difference calculus; Graham, Knuth
> & Patashnik, *Concrete Mathematics* ch. 2, for the modern treatment.

---

## Volume II — Eighth Grade: The Lattice Plane

*Traditional: linear equations · introduction to functions · the Pythagorean theorem ·
transformations and similarity · exponents and scientific notation · systems ·
volume of cones and spheres*

1. The Grid Has No Gaps in It
2. Quadrance — squared distance, so no square root ever appears
3. Pythagoras Without a Square Root
4. Which Numbers Are Hypotenuses? — sums of two squares
5. A Circle Is a Set of Dots
6. Drawing a Circle With Nothing but Addition — the midpoint algorithm
7. Counting Your Way to π — the Gauss circle problem
8. Pick's Theorem — the area of any lattice polygon, by counting its dots
9. Spread — turning, measured without trigonometry

> *Credits:* Wildberger, *Divine Proportions* (2005), for quadrance and spread.
>
> The circle-drawing algorithm here is the **midpoint circle algorithm** (`d = 3 − 2r`).
> Read the primary source before crediting it: Bresenham's *A Linear Algorithm for
> Incremental Digital Display of Circular Arcs*, CACM 20(2), Feb 1977, 100–106, uses a
> **different** decision variable — evaluated at the diagonal neighbour, initialised
> `2 − 2R`. The two agree on output but are not the same procedure, so the near-universal
> name "Bresenham's circle algorithm" for the `3 − 2r` form is a misattribution. (And the
> famous 1965 IBM Systems Journal paper draws lines, not circles.) Also: Gauss for the
> circle problem; Fermat and Jacobi for two squares; Pick (1899).

---

## Volume III — Ninth Grade: Turning

*Traditional Algebra I: linear, quadratic and exponential functions · factoring ·
polynomials · radicals · systems of equations*

1. Turning Without Angles
2. The Rotation Rule — `(a,b) ⋆ (u,v) = (au − bv, av + bu)`
3. You Cannot Get Off the Circle — closure, and why it's a group
4. Exact Turns — Pythagorean triples as rotations that land perfectly
5. Every Exact Turn There Is — the rational parametrization
   `((1−t²)/(1+t²), 2t/(1+t²))`, which emits the triples of Volume II on demand
6. The Spread Laws — the rational replacements for the sine and cosine rules
7. Spread Polynomials — multiple turns are *polynomials* in a single turn, so
   `cos nθ` is algebra rather than analysis (Chebyshev's polynomials, in disguise)
8. Polynomials Are Difference Tables
9. The Right Kind of Power — falling factorials, and the return of `Δx⁽ⁿ⁾ = n·x⁽ⁿ⁻¹⁾`
10. Newton's Series — every polynomial rebuilt from its differences at zero, in
    finitely many terms, exactly

> *Chapter 7 is the book's hinge.* The familiar power rule visibly **fails** on ordinary
> powers (`Δx² ≠ 2x`), and then comes back perfect on the right basis. Break it, then
> fix it.

> *Credits:* Chapters 6–8 are *Concrete Mathematics* ch. 2 and 5, reordered for a reader
> who has not met calculus. The falling-factorial notation and its treatment are theirs.
> Wildberger (2005) for chapters 1–5.

---

## Volume IV — Tenth Grade: Proof, and Other Finite Worlds

*Traditional Geometry: formal proof · congruence and similarity · right-triangle
trigonometry · circles · coordinate geometry · volume*

1. Induction — the only proof engine we need
2. Why Collapsing Sums Always Collapse
3. Clock Arithmetic
4. Circles on a Clock — `p − 1` points, or `p + 1`, and why `−1` decides
5. Why That Circle Doesn't Look Like a Circle — equidistribution, honestly
6. Two Finite Worlds — a quotient is not an approximation
7. Quadrance and Spread Over Any Field — the same formulas, on a clock
8. What We Gave Up — no order, no distance, no betweenness

> *Volume IV is where the book earns trust.* Chapters 5 and 8 admit what the approach
> cannot do. A curriculum that only shows its wins is the thing we're replacing.

---

## Volume V — Eleventh Grade: Growth

*Traditional Algebra II / Precalculus: polynomial and rational functions · exponentials
and logarithms · sequences and series · trigonometric functions · conics · matrices ·
vectors*

1. Doubling — `Δ2ˣ = 2ˣ`, so **2** is this world's `e`
2. Every Other Base — `Δbˣ = (b − 1)bˣ`, and why 2 is the only fixed point
3. Letters in the Wrong Envelopes — `n` letters, `n` envelopes, nobody gets their own.
   Count the ways; `n!/Dₙ` marches to **e**. The same trick that gave us π, on a
   different pile of things to count
4. e, to as Many Digits as You Ask For — partial sums of `1/k!` are exact fractions
   and the leftover is smaller than `1/(n·n!)`, so every answer arrives with a receipt
5. Undoing Growth — discrete logarithms
4. Summation by Parts
5. Generating Functions — power series with no convergence question, because nothing
   is ever evaluated
6. Recurrences and Closed Forms
7. Tables With Two Indices — matrices as bookkeeping
8. Conics on a Lattice

> *Credits:* Chapters 4–6 are *Concrete Mathematics* ch. 7 and 8 — generating functions
> and recurrences — at a slower pace. Chapter 5 is the one place this book gets something
> for free that the continuous route pays dearly for: a generating function is never
> evaluated, so convergence never arises.

---

## Volume VI — Calculus, Finitely

*Traditional AP Calculus AB/BC: limits and continuity · derivatives and applications ·
integrals · the Fundamental Theorem · series · parametric and polar (BC)*

1. The Tolerance Game — you name the error you'll accept, I hand you the `N`. A
   procedure, introduced as a game, not a mystery
2. Refining the Grid — `h` gets smaller; it never "reaches" zero
3. The Difference Quotient
4. When Refinement Settles Down, and When It Doesn't
5. Sums Become Integrals
6. The Fundamental Theorem, Twice — the telescoping version you proved in Volume I,
   and the continuous shadow it casts
7. Taylor From Newton — the series that used to stop, and what breaks when it doesn't
8. Where We Must Borrow — the intermediate value theorem fails constructively; here is
   the weaker true thing, and here is what it costs

> *Credits:* Bishop, *Foundations of Constructive Analysis* (1967), for chapters 4 and
> 8; Weihrauch, *Computable Analysis* (2000), for the tolerance game.

---

## Coda — A Gesture at More Variables

Not a course. Four chapters to show the machinery keeps working.

1. Grids in Three Dimensions
2. Partial Differences
3. Volume by Counting — double sums
4. Green's Theorem Is Bookkeeping — the discrete version, where it's an accounting
   identity rather than a theorem

> Note on scope: AP Calculus BC is still **single-variable** — its extra material is
> series, parametric and polar. Genuinely multivariable work is post-AP. This coda is
> a flourish, and should be labelled as one.

---

## Volume VII — The Continuous Dialect

**Not an appendix.** An earlier draft of this document called it one, on the assumption
that a finite reader needs only new notation. That is false, and the error is worth
recording: the gap is partly conceptual, and one part of it is large.

### What comes free — the same idea, renamed

| This book | The usual notation |
|---|---|
| `Δf` | `f′` |
| `Σ` | `∫` |
| telescoping | the Fundamental Theorem |
| finite sums | Riemann sums |
| summation by parts | integration by parts |
| difference equations | Euler's method, slope fields |
| the tolerance game | `ε`–`N` |
| quadrance `Q` | `d²` |
| spread `s` | `sin²θ` |

On this half the reader arrives **ahead** of a traditional student. Riemann sums and
Euler's method are what they have been doing since Volume I.

### What must be relearned — same concept, different shape

1. The Power Rule Again — `Δx⁽ⁿ⁾ = n·x⁽ⁿ⁻¹⁾` becomes `d/dx xⁿ = n·xⁿ⁻¹`; the basis
   changes back
2. The Product Rule Loses Its Shift — discretely it is `Δf·g(x+1) + f·Δg`, which is
   *not* symmetric; continuously the shift vanishes and it is
3. Quotients, and Why They Were Ugly Before

### What is genuinely missing — new machinery

An earlier draft listed `e` and the trigonometric functions here. That was wrong, and
the mistake is instructive enough to keep in the book. **The objects are all reachable
finitely.** `e` is a counting problem about envelopes; sine and cosine are the rational
parametrization of the circle, the spread polynomials, and the rotation group, all of
them exact. What needs the limit is not the objects but the *differential relationships
between them*.

4. The Chain Rule — there is no clean general discrete analogue, so this is built from
   scratch. It is also the most-used tool on the exam.
5. Radians, and Why the Angle Had to Change — `d/dx sin x = cos x` is false in degrees
   and true in radians, and radian measure is defined by arc length. This is the one
   place the continuum is genuinely unavoidable, and it is worth dwelling on
6. Why the Natural Base Moved — it was 2 for `Δ`, it is `e` for `d/dx`. Same question,
   different operator, different answer
7. Logarithms of the Continuous Kind
8. Limits of Functions — one-sided, at infinity, L'Hôpital
9. **Series That Do Not Stop** — the longest chapter in the book, and the only really
   large gap. Everything until now terminated. Convergence tests, radius of
   convergence, and why Newton's series became Taylor's problem
10. Continuity and the Intermediate Value Theorem — the classical statement, the
    constructive one from VI.8, and an honest account of the difference

> **Honest accounting.** A reader finishing Volume VI arrives already owning `π`, `e`,
> sine and cosine as *objects*, with the structural half of calculus unusually solid.
> What they lack is the differential calculus of those objects, and convergence.
> Chapter 9 is the real work; the rest is smaller than it looks.

---

## Known weak joints

Stated up front so a prototype can attack them first.

- **Chapter II.9 and the whole spread strand.** Reviewers of *Divine Proportions*
  granted its coherence but questioned whether quadrance and spread are actually
  *easier* for ordinary students. Since "easier" is this book's entire claim, this is
  the first chapter to write and test, not the last.
- **Radian measure** is the single genuinely unavoidable appeal to the continuum. Every
  other apparent obstacle turned out to be reachable by counting or by algebra; this one
  did not. `π` and `e` as *numbers* are fine — they are procedures with error
  certificates. It is `d/dx sin x = cos x`, which needs arc length, that has no finite
  route.
- **Convergence.** The one large gap, and the whole of VII.9. Everything in Volumes I–VI
  terminates, which is the book's chief pleasure and also why its reader meets an
  infinite series for the first time in the last hundred pages.
- **The exit ramp.** A reader who does only this book would walk into the AP Calculus
  exam having never evaluated a limit in the notation the test is written in. The
  appendix is not optional decoration; it is what makes the book usable.
