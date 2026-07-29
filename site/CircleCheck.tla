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

`GoodSpecHolds` verified by TLC at R = 3, 5, 8, 13, 21, 34, 55. It now includes
`NoTies`, separately checked at R = 3, 5, 8, 13, 21, 34, 55, 89.

`NoTies` is the one property here with a proof as well as a check: two dots one
apart give totals summing to an odd number, and twice the target is even, so the
two can never be equal. TLC confirms it radius by radius; the parity argument
settles it for all of them at once.

`BadDrawingIsCorrect` is where it gets interesting. The sabotage breaks **103 of the 118
radii from 3 to 120**, always by failing `Sound` — it draws a dot that was not allowed.
But it *passes* at 3, 4, 5, 6, 7, 9, 10, 11, **13**, 17, 18, 19, 28, 31 and others.

Thirteen is the radius used throughout the lesson. Checking one case would have declared
the broken program correct.

`DrawingIsThinner` is false at R = 5 and true from R = 13 up, for the reason given at the
end of `Circle.tla`.
