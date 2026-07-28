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

The drawing algorithm this specifies is Bresenham's circle algorithm:

> J. E. Bresenham, "A Linear Algorithm for Incremental Digital Display of Circular
> Arcs", *Communications of the ACM* 20(2), February 1977, 100–106.

Not the better-known 1965 paper — "Algorithm for computer control of a digital
plotter", *IBM Systems Journal* 4(1), 25–30 — which draws **lines**. The circle came
twelve years later. The variant used here is usually called the *midpoint circle
algorithm*.

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
    (*  "no more than half a step off the ring".
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
=============================================================================
```

## Notes

`Sound` and `Complete` are genuinely different claims, and the drawing is a *strict*
subset of `Circle` at any interesting radius — at `R = 13` the blueprint permits 88 dots
and Bresenham selects 72 of them. A specification says what is allowed; it does not say
what you must pick.

At `R = 5` the two happen to coincide: the algorithm takes all 28. So "strictly thinner"
is false at small radii, which is worth knowing before asserting it as an invariant.
