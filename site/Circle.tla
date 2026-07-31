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

CONSTANT R              \* the radius: a whole number
CONSTANT Slack          \* how much worse than the best we will still accept

Dots == (-R..R) \X (-R..R)

Total(p) == p[1]*p[1] + p[2]*p[2]
    (*  No distances live in this module. We compare squared totals, because
        asking how far a dot is takes you to a number that is not there.  *)

Gap(p) == LET d == Total(p) - R*R IN IF d < 0 THEN -d ELSE d
    (*  how far this dot's total misses the one we want  *)

Circle == { p \in Dots :
              \A q \in Dots :
                (q[1] = p[1]) => Gap(p) =< Gap(q) + Slack }
    (*  A dot is on the circle if no other dot in its column beats it by more
        than Slack. With Slack = 0 that is exactly "the nearest one" and the
        ring is one dot thick.  *)
====
```

## Notes

`Slack` is the price of a bolder line, and it is not free.

With `Slack = 0` every kept dot is the nearest in its column, and the two gaps
either side of the ring make one unit between them, so nothing is more than
**half a unit** off. That is the promise the lesson makes.

Widening it costs exactly what you would expect. A dot's gap can now exceed the
best by `Slack`, and a gap of `g` puts you roughly `g / 2R` from the true ring,
so the worst case becomes

    1/2  +  Slack / 2R

Measured, against radii 12, 30 and 60: at `Slack = 0` the worst dot is 0.46 units
out; at `Slack = R` it is 0.73 against a bound of 1.0; at `Slack = 2R`, 1.45
against 1.5. The bound holds and is not tight, which is what you want from a
bound.

So `Slack = R` doubles the promise, from half a unit to one. Anything drawn that
way is still a circle, but it is a circle you have agreed to be twice as wrong
about, and the lesson should say so out loud rather than quietly enjoying the
thicker line.
