# CircleCheck — does the drawing actually satisfy the blueprint?

Literate, like `Circle.tla`, and under the same two constraints: the file must be named
`.tla`, and prose brackets the module rather than interleaving it.

Run it with:

```
tlc CircleCheck.tla
```

using `CircleCheck.cfg` to set the radius and choose an invariant.

The algorithm appears here as a recursive function so TLC can evaluate it. **This is the
only place in either file where an order of steps exists.** `Circle` itself has none —
that is the distinction the whole exercise is about.

The algorithm below is the **midpoint** variant, `d = 3 - 2r` -- not the one in
Bresenham's 1977 paper, which uses a different decision variable initialised `2 - 2R`.
See `Circle.tla` for the full attribution and for why the difference matters to the
tie question.

## The module

```tla
-------------------------- MODULE CircleCheck --------------------------
EXTENDS Circle

VARIABLE tick                 \* TLC wants a state machine; this one does nothing
Init == tick = 0
Next == UNCHANGED tick
Spec == Init /\ [][Next]_tick

    (*  The midpoint circle algorithm, transliterated. Walks one octant
        and mirrors as it goes.  *)

Mirrors(p) ==
    { <<p[1], p[2]>>, <<p[2], p[1]>>, <<-p[1], p[2]>>, <<-p[2], p[1]>>,
      <<p[1], -p[2]>>, <<p[2], -p[1]>>, <<-p[1], -p[2]>>, <<-p[2], -p[1]>> }
    \* the eight images of a dot under the symmetries of the sheet

RECURSIVE Walk(_, _, _, _)
Walk(x, y, d, acc) ==
    IF x > y
      THEN acc
      ELSE LET acc2 == acc \cup Mirrors(<<x, y>>)
           IN  IF d < 0
                 THEN Walk(x + 1, y,     d + 4*x + 6,        acc2)
                 ELSE Walk(x + 1, y - 1, d + 4*(x - y) + 10, acc2)

Drawn == Walk(0, R, 3 - 2*R, {})

    (*  The same thing, sabotaged: one constant changed, 6 into 4. This is
        the difference nobody in the class could find by reading.  *)

RECURSIVE WalkBad(_, _, _, _)
WalkBad(x, y, d, acc) ==
    IF x > y
      THEN acc
      ELSE LET acc2 == acc \cup Mirrors(<<x, y>>)
           IN  IF d < 0
                 THEN WalkBad(x + 1, y,     d + 4*x + 4,        acc2)
                 ELSE WalkBad(x + 1, y - 1, d + 4*(x - y) + 10, acc2)

DrawnBad == WalkBad(0, R, 3 - 2*R, {})

    (*  What we ask TLC to confirm.  *)

    (*  What a drawing owes us. A "drawing" is whatever set of dots somebody's
        program produced; these say when it was allowed to produce them. They
        live here and not in Circle, because they are about checking, and
        Circle is only about saying what the thing is.  *)

Sound(drawn)     == drawn \subseteq Circle
    \* every dot it drew was permitted

Complete(drawn)  == \A x \in -R..R : \E p \in drawn : p[1] = x
    \* it left no column empty

Symmetric(drawn) == \A p \in drawn : Mirrors(<<p[1], p[2]>>) \subseteq drawn
    \* whatever it drew, it drew all eight mirrors of

Correct(drawn) == Sound(drawn) /\ Complete(drawn) /\ Symmetric(drawn)

CircleIsSymmetric == Symmetric(Circle)
CircleIsComplete  == Complete(Circle)
DrawingIsCorrect  == Correct(Drawn)
DrawingIsThinner  == Drawn \subseteq Circle /\ Drawn # Circle

GoodSpecHolds == /\ CircleIsSymmetric
                 /\ CircleIsComplete
                 /\ DrawingIsCorrect
                 /\ NoTies

BadDrawingIsCorrect == Correct(DrawnBad)
=============================================================================
```

## Results on record

Re-derived after the specification was corrected. `Circle` once meant the half-unit
*band*; it now means *least in its column, or least in its row*, which is what the
program had been doing all along while the module said otherwise. Everything below is
against the corrected meaning.

`GoodSpecHolds` verified by TLC at R = 3, 5, 8, 13, 21, 34, 55.

**R = 89 was abandoned after thirty-one minutes**, and that is worth more than the seven
successes. `Circle` quantifies over every pair of dots on the sheet, so the work grows
like `R⁴`; at 89 there are 32,041 dots and about a billion pairs. The check does not
scale, and there is no radius at which it stops being a check of *that one radius*.

Ralphie's parity argument settles every radius, at every size, in two lines, and runs in
no time at all because it does not run. That is the whole case for keeping a proof next
to a check, stated in wall-clock seconds rather than in philosophy — which is why the
argument lives in `Circle.tla` and not only here.

`NoTies` is checked directly instead at every radius from 1 to 200, every column, every
pair of dots one apart: **no ties, anywhere**.

`board_program.circle(R)` equals `Circle` **exactly** — not a subset, the same set — at
every radius from 1 to 200. That is the claim the lesson's colophon makes, and it is now
true; before the correction the program drew 20 dots at R=12 that the module forbade,
all of them nearest in their row on the steep sides.

`BadDrawingIsCorrect` is where it gets interesting. One constant changed, 6 into 4 — the
difference nobody in the class could find by reading. It breaks **114 of the 118 radii
from 3 to 120**, always by failing `Sound`: it draws a dot that was not allowed.

But it *passes* at **3, 5, 7 and 10**.

So a check does catch this bug, and would have caught it at the radius this lesson uses.
What it would not have caught is the same bug checked at a radius small enough to fit on
a board — which is exactly the radius somebody in a hurry picks. The check is not
worthless and it is not sufficient; it is only as good as the case you thought to try,
and you cannot tell from inside the check whether you thought of a good one.

*(An earlier version of this note recorded 103 of 118, passing at thirteen among others.
That was correct against the old band definition and is kept here as a record of what
changing a specification does to every result downstream of it.)*
