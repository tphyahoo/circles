# Circle — what a circle *is*, on a sheet of dots

This file is literate. Everything before the MODULE header line, and everything after
the row of equals signs that ends it, is invisible to the TLA+ tools — so prose and
code fences out here cost nothing.

Three constraints, each learned the hard way:

- It must be named `.tla`. SANY rejects `.md` outright — it appends `.tla` and looks for
  that file, so the module simply isn't found.
- Prose can **bracket** the module but not **interleave** it. Everything between the
  header line and the terminator is parsed as TLA+, so commentary inside has to be a
  TLA+ comment, not a Markdown paragraph.
- **Never write the marker tokens in the prose.** SANY scans for the first header line
  in the file and does not know what a backtick is. Quoting the markers, even inside
  code formatting, makes the parser try to open a module there and fail.

Nothing here says **how** to draw a circle. That is the whole point. This is the
blueprint; the Python is the particle board.

## Credits

The algorithm taught here is the **midpoint circle algorithm**, initialised
`d = 3 - 2r`. It is almost universally called "Bresenham's circle algorithm", and that
attribution is wrong in a way worth recording.

Bresenham's actual 1977 paper --

> J. E. Bresenham, "A Linear Algorithm for Incremental Digital Display of Circular
> Arcs", *Communications of the ACM* 20(2), February 1977, 100-106

-- uses a different decision variable. His is evaluated at the *diagonal* neighbour,
`Delta = [(X+1)^2 + (Y-1)^2] - R^2`, initialised `Delta_0 = 2 - 2R`, with three moves
rather than two. The two algorithms agree on their output -- his quarter-arc points sit
inside the midpoint octant and its mirrors at every radius tested to 200 -- but they are
not the same procedure, and `3 - 2r` is not his.

(And not the famous 1965 paper either: "Algorithm for computer control of a digital
plotter", *IBM Systems Journal* 4(1), 25-30, draws **lines**.)

On ties, the paper is worth reading before anyone repeats what this file used to
say. Our midpoint `d` is always odd, so it never lands on zero, and the `else` branch
never breaks a tie. That is a fact about the *midpoint* variant only.

Bresenham's own `Delta` **does** hit zero -- at 143 of the radii from 2 to 399 -- and he
handles it explicitly:

> "(c) If Delta_i = 0 then (X+1, Y-1) is on the true circle, i.e. case 5, and the
> movement should be m2. In this case the above steps yield delta > 0 and delta' < 0 so
> a proper m2 move is forced by either calculation."

His `Delta` is zero exactly when `(X+1)^2 + (Y-1)^2 = R^2` -- when a lattice point lands
*perfectly* on the ring. So the radii where his algorithm meets the case are precisely
the ones carrying whole-number triangles: 5, 10, 15, 17, 20, 25, 29, 30, 34, 35, ...

He did not dodge the case. He found it, named it, and proved it was unambiguous.

On writing the blueprint before the program at all, and on a specification not being
written in the material the thing is built from:

> Leslie Lamport, "Thinking Above the Code", Microsoft Research Faculty Summit, 2014.

## The module

```tla
---------------------------- MODULE Circle ----------------------------
EXTENDS Integers

CONSTANT R                          \* the radius: a whole number

Dots == (-R..R) \X (-R..R)          \* every dot on the sheet

Quadrance(p) == p[1]*p[1] + p[2]*p[2]
    (*  Squared distance. No square root appears anywhere in this module,
        and the reason is that we never need one.  *)

NearRing(p) ==
    (*  "no more than half a unit off the ring".
          |Sqrt(Q) - R| =< 1/2
        is the same claim as
          (2R-1)^2 =< 4Q =< (2R+1)^2
        which stays entirely in whole numbers.  *)
    /\ (2*R - 1)^2 =< 4 * Quadrance(p)
    /\ 4 * Quadrance(p) =< (2*R + 1)^2

Circle == { p \in Dots : NearRing(p) }
    (*  THE DEFINITION, and all of it. Note what is absent: any order of
        steps, any loop, any decision about which dot to visit first.
        A set does not have a beginning.  *)

Mirrors(p) ==
    { <<p[1], p[2]>>, <<p[2], p[1]>>, <<-p[1], p[2]>>, <<-p[2], p[1]>>,
      <<p[1], -p[2]>>, <<p[2], -p[1]>>, <<-p[1], -p[2]>>, <<-p[2], -p[1]>> }

    (*  What a drawing owes us. A "drawing" is whatever set of dots
        somebody's program produced; these say when it was allowed to
        produce them.  *)

Sound(drawn)     == drawn \subseteq Circle
    \* every dot it drew was permitted

Complete(drawn)  == \A x \in -R..R : \E p \in drawn : p[1] = x
    \* it left no column empty

Symmetric(drawn) == \A p \in drawn : Mirrors(p) \subseteq drawn
    \* whatever it drew, it drew all eight mirrors of

Correct(drawn) == Sound(drawn) /\ Complete(drawn) /\ Symmetric(drawn)

    (*  "take the nearest" only names a dot if there is never a tie. A tie in
        column x between the dots at y and y+1 would mean their two totals sat
        the same distance either side of the target, i.e.

              (R^2 - Q1)  =  (Q2 - R^2)      i.e.   Q1 + Q2  =  2*R^2

        It never happens, and not by luck: Q1 + Q2 is
        2x^2 + y^2 + (y+1)^2 = 2x^2 + 2y^2 + 2y + 1, which is always ODD,
        while 2*R^2 is always EVEN.  *)

NoTies == \A x \in -R..R : \A y \in -R..R :
            LET Q1 == x*x + y*y
                Q2 == x*x + (y+1)*(y+1)
            IN  Q1 + Q2 # 2*R*R
=============================================================================
```

## Notes

`Sound` and `Complete` are genuinely different claims, and the drawing is a *strict*
subset of `Circle` at any interesting radius — at `R = 13` the blueprint permits 88 dots
and Bresenham selects 72 of them. A specification says what is allowed; it does not say
what you must pick.

At `R = 5` the two happen to coincide: the algorithm takes all 28. So "strictly thinner"
is false at small radii, which is worth knowing before asserting it as an invariant.
