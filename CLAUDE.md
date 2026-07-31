# circles

Visualising circles over finite structures, plus a set of writing pieces built on top
of the maths. Started from an AI-generated lesson transcript (`google_ai_tab_dump.txt`)
that turned out to be substantially wrong; most of the work here is checking it.

This directory is also an **Obsidian vault** — the `.md` files are notes, so relative
image links (`![](ring_29_3.png)`) must keep resolving. Don't move images away from the
markdown that references them.

## Layout

The active work is the lesson in `site/`. The root holds the original modular-circle
plotter and the earlier writing.

| Path | What |
|---|---|
| `docs/index.html` | **Days one and two.** Generated — never edit directly. Pages serves this. |
| `docs/counting.html` | **Day three**, a separate document so it can be cut cleanly. Also generated. |
| `site/build_v2.py` | Generates **both** pages from `DOC1` and `DOC2`. Edit this. Images inline from `site/plates/`. |
| `site/board.py` | The **board** figures — Mrs. Feeney's whiteboard. Writes into `plates/`. |
| `site/screen.py` | The **screen** figures — projector output. Writes into `plates/`. |
| `site/Circle.tla` | The blueprint: what a circle *is*, plus `NoTies`. Literate; read its header. |
| `site/CircleCheck.tla` | The drawing transliterated, plus a sabotaged variant, for TLC. |
| `site/CircleCheck.cfg` | TLC config — set the radius and pick an invariant here. |
| `site/lattice_circle.py` | The drawing in Python, with the blueprint's invariants as asserts. |
| `site/no_floats.py` | Proves `lattice_circle.py` is integer-only. Exits non-zero if not. |
| `site/day-one-circles-v1-ministry.html` | Abandoned first version, `F_p` framing. Reference only. |
| `circles.py` | The modular-circle plotter. `python3 circles.py` opens one window. |
| `day-one-circles.md`, `day-one-dialogue.md` | Earlier writing on the `F_p` material. |
| `docs/table-of-contents.md` | Outline for the whole book, 7th grade through calculus. |
| `google_ai_tab_dump.txt` | The original transcript. Source of the errors, not a reference. |

**Two visual registers, and the distinction is the argument, not decoration.** The board
is a whiteboard with a printed dot lattice: printed things (lattice, axes, numerals) are
precise and faint, anything drawn on top is marker and wobbles. The screen is the
projector: machine output only. `board.py` enforces this — only marker artists get
sketch params. Figures are numbered `Fig. N` in one sequence by document position, so
inserting one renumbers the rest automatically.

To rebuild everything: `python3 board.py && python3 screen.py && python3 build_v2.py`
from `site/`.

### Publishing

Two published copies, and they are different things:

- **GitHub Pages** — https://tphyahoo.github.io/circles/ and `/counting.html` — served from `docs/`
  on every push to `main`. This is the public one. Nothing to do but push.
- **Claude artifact** — https://claude.ai/code/artifact/fac3d388-297f-4604-a7ef-e66563567d6e

To update it from a **new session**, call Artifact with `docs/index.html` **and pass that
URL as `url`**. Without the `url` parameter a fresh conversation mints a brand
new artifact and the link above goes stale — the original was published from a
session-scoped scratchpad path that no longer exists.

Note: the board figures are **not byte-reproducible.** `path.sketch` gives the marker its
wobble and is not seeded, so re-running `board.py` changes the PNGs cosmetically and the
page size drifts by a kilobyte or two. That is expected. Do not go looking for a content
diff, and do not seed it away — the variation is what stops the figures looking
machine-drawn.

## Facts worth not rediscovering

- `circles.py` originally **never ran** — matplotlib's mathtext has no `\pmod`, so the
  title raised `ParseFatalException` every time. Use `\mathrm{mod}` longhand.
- The generator is O(p) (bucket each `y` by `y² mod p`, look up roots of `r²−x²`).
  Verified identical to brute force on every residue of every prime ≤ 257. Do not
  "simplify" it back to the double loop — p=65537 goes from <1s to hours.
- Point counts: `p−1` when `p ≡ 1 (mod 4)`, `p+1` when `p ≡ 3 (mod 4)`, for `c ≠ 0`.
  At `c = 0`: `2p−1` (two crossed lines) versus `1` (origin alone).
- **Big primes look worse, not better.** The points equidistribute, so p=65537 is dust.
  The best-looking circle is `p=29, c=3` (24 of 28 points on one ring); `p=17, c=7`
  is 100% but sparse. Searched every residue of every prime < 600.
- A modular circle is *not* a discretised circle. `ℤ/p` has no order or metric —
  reduction mod p is a quotient, not an approximation. For a picture that actually
  looks like a circle, use a bounded integer lattice (see `two_finite_worlds.png`).

### About the lesson specifically

- **The characteristic error of this material is a decimal that quietly needs a square
  root.** It surfaced four separate times: gaps written as 0.42/0.58, a worst-case error
  of 0.48 (twice), and Popovich evaluating √48 ≈ 6.9. Each looked like harmless
  precision. Before writing any number into the lesson, ask whether getting it requires
  the operation the lesson refuses.
- The classroom does not use the words "square root". Popovich tries and is stopped —
  *"that way lie paradoxes… not today, anyway."* The frame around the lesson (captions,
  colophon) may use the term; the room may not.
- **`3 − 2r` is NOT Bresenham's algorithm.** It is the midpoint variant. Bresenham's 1977
  CACM paper uses a decision variable at the diagonal neighbour, initialised `2 − 2R`,
  with three moves. They agree on output but are different procedures. His Δ *does* hit
  zero — at 143 of the radii 2..399 — and he handles it as his "case 5". It is zero
  exactly at the Pythagorean radii, which is why §03 plants a promise that §05 pays off.
- `NoTies` has a proof as well as a check: two dots one apart give totals summing to an
  odd number, twice the target is even. TLC verifies it one radius at a time; the parity
  argument settles all of them. Do not delete the proof in favour of the check.
- Everything in the page is verified before being written. The colophon says so, which
  means it has to stay true.

## Toolchain

Installed locally under `~/.local`, no sudo, nothing system-wide:

- Temurin JRE 21 — `~/.local/lib/jdk-21.0.11+10-jre/`
- `tla2tools.jar` — `~/.local/lib/`
- `tlc` and `sany` wrappers — `~/.local/bin/` (already on PATH)

Model-check with `tlc CircleCheck.tla` from `site/`, editing `CircleCheck.cfg` to set
the radius and pick an invariant. All of this works offline.

Not yet installed, and wanted: **VS Code plus the official `tlaplus.vscode-tlaplus`
extension.** The TLA+ Toolbox is in maintenance mode; the project recommends the VS Code
extension instead. It needs network to install, and will use the Java above.

Obsidian will not render the `.tla` files and does not index symlinks — symlinked `.md`
companions were tried and removed. Once VS Code is in, the split is: specs there, notes
in Obsidian, and no workaround is needed. Do not build an `.md`-to-`.tla` sync step.

## What this lesson is, and is not

**It is about saying what the mathematics is, and then doing it the obvious way.
It is not about doing it fast.**

- **Say what the thing IS**, precisely, in the shortest notation that cannot be
  misread. That is what the TLA+ is for. Not specification-as-professional-practice
  — just legibility. It is shorter and harder to misread than the Python.
- **Then compute it the stupid way.** Try everything, keep what fits. The naive
  method is the one the class can write, check, and believe.
- **Efficient implementation is a different class.** Running totals, magic
  constants, exploiting symmetry to compute one eighth and mirror the rest — none
  of that belongs here. If it appears at all it appears as something *deferred*:
  "there is a faster way, it gets the same dots, that is another lesson."

Why: every time efficiency material has gone in, it has crowded out the
mathematics and then generated questions the lesson has to stop and answer —
where did the 6 come from, why one eighth, what is the running number. Those are
good questions about a subject this lesson is not teaching. The tell is that the
answer is always "bookkeeping" or "grind through the algebra", which is exactly
the kind of thing this lesson refuses to say about anything else.

Corollary: prefer a picture of the result over a procedure for getting there.

## Working conventions

- **Run scripts by path, not as inline one-liners.** Write throwaway analysis to a file
  and run `python3 <path>`; set env vars like `MPLBACKEND` inside the script and do
  output filtering in Python rather than piping through `grep`. Inline commands with
  `VAR=x` prefixes or pipes miss the permission allowlist and cause approval prompts.
- Verify numeric claims by computing them before writing them down. Nearly every error
  in the source transcript was a plausible-sounding number nobody checked.

### The board program

`site/board_program.py` is the single source of truth for the code in the lesson.
`build_v2.py` reads it and prints it into the page; `photograph.py` runs it and
captures its stdout — colour codes and all — into the figure. There is no second
implementation, so the picture cannot drift from the code beside it.

That was not true for most of this project's life: the figures came from
matplotlib in `screen.py` while the page showed hand-written code, so the lesson
claimed "here is the program and here is what it prints" and it was not so. If
you add another program to the lesson, add it the same way.
