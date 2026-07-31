# circles

**Work in progress.** One eighth-grade maths lesson, its specification, and the checking
that produced both.

### → [Read the lesson](https://tphyahoo.github.io/circles/)

(GitHub shows HTML as source, so the link above goes to the rendered page.)

---

## What this is

A lesson called *Circles, and How Wrong We're Willing to Be*, set in a world where the
plane is a lattice of dots with nothing in between them. A circle is the dots nearest a
given distance from the middle. Nobody measures anything, nothing is infinite, and π
turns up at the end anyway — by being counted.

It started as a fact-check. Someone generated a classroom transcript about "ultrafinite
circles" with an AI, and it was confidently wrong about roughly seven things. That
transcript is here as `google_ai_tab_dump.txt`, kept as the source of the errors rather
than as a reference. Most of what followed is the checking.

## What's actually finished

The **mathematics** is done, and none of it is asserted without being computed:

- Every number in the lesson was calculated before it was written down.
- The blueprint is in TLA+ (`site/Circle.tla`) and model-checked with TLC.
- The Python (`site/lattice_circle.py`) carries the same invariants as assertions, and
  `site/no_floats.py` proves it never leaves the integers — statically by walking the
  syntax tree, dynamically by checking every value it produces.
- Where something is checked rather than proved, the text says so.

Two findings worth the trouble:

**A wrong program is not wrong everywhere.** A one-character sabotage of the drawing
algorithm is wrong at 103 of the 118 radii from 3 to 120 — and *right* at 13, which is
the radius the lesson uses throughout. Testing one case would have shipped it.

**`d = 3 − 2r` is not Bresenham's algorithm.** It is the midpoint variant. Reading the
actual 1977 CACM paper shows his decision variable is evaluated at the diagonal
neighbour and initialised `2 − 2R`, with three moves rather than two. They agree on
output but are different procedures. His decision variable *does* hit zero — at 143 of
the radii from 2 to 399 — and he handles it explicitly as his "case 5", which is the
opposite of what everyone assumes. It is zero exactly at the Pythagorean radii.

## What isn't finished

**The voice.** It reads like a transcript of an argument that went well on the first
take, which is not what a classroom sounds like. Measured against the text itself:
no student stays confused for more than a single turn; one line in the whole lesson is
off-topic; every one of Ralphie's forty turns ends in complete punctuation; and there
are thirty one-liners in a hundred and sixty-six turns. The students are currently
functions rather than people. That pass hasn't happened.

**More figures.** There are eighteen. Several moments still have Mrs. Feeney writing on
the board with nothing shown.

**The book.** `docs/table-of-contents.md` sketches seven volumes from seventh grade
through calculus. That is a map of a territory, not a commitment to walk it.

## Reading it

The lesson is a single self-contained HTML file, served at
[tphyahoo.github.io/circles](https://tphyahoo.github.io/circles/) and built to
`docs/index.html`. Everything is inlined, including the figures, so the file works
offline and from disk.

To rebuild everything from source, from `site/`:

```
python3 board.py && python3 screen.py && python3 build_v2.py
```

To model-check the specification (needs Java and `tla2tools.jar`):

```
tlc CircleCheck.tla
```

`CLAUDE.md` has the file map, the two visual registers, and the traps worth not
rediscovering.

## Credits

None of the mathematics is new. The circle-drawing is the midpoint algorithm, descended
from Bresenham (CACM 20(2), 1977, 100–106). Counting dots to get π is the Gauss circle
problem. Which radii carry perfect hits is Fermat and Jacobi on sums of two squares.
Writing the blueprint before the program, and the observation that a specification is
not written in the material the thing is built from, is Leslie Lamport. Quadrance and
spread are Wildberger's. The nearest existing book is Graham, Knuth and Patashnik's
*Concrete Mathematics*.

The only thing arranged here is the order.
