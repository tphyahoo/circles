# circles

Visualising circles over finite structures, plus a set of writing pieces built on top
of the maths. Started from an AI-generated lesson transcript (`google_ai_tab_dump.txt`)
that turned out to be substantially wrong; most of the work here is checking it.

This directory is also an **Obsidian vault** — the `.md` files are notes, so relative
image links (`![](ring_29_3.png)`) must keep resolving. Don't move images away from the
markdown that references them.

## Layout

| Path | What |
|---|---|
| `circles.py` | The plotter. Run `python3 circles.py` → opens one window, writes nothing. |
| `day-one-circles.md` | Straight reference write-up of the real mathematics. |
| `day-one-dialogue.md` | Classroom-dialogue version (Mrs. Feeney / Ralphie / Popovich). |
| `site/day-one-circles.html` | Published page — the "half-dot" lesson set on a lattice. |
| `site/day-one-circles-v1-ministry.html` | Earlier version, `F_p` framing, kept for reference. |
| `site/build_v2.py`, `site/build_page.py` | Rebuild those pages; images inline from `site/plates/`. |
| `*.png` (root) | Figures referenced by the markdown notes. |
| `google_ai_tab_dump.txt` | The original transcript. Source of the errors, not a reference. |

Published artifact: https://claude.ai/code/artifact/fac3d388-297f-4604-a7ef-e66563567d6e
(republish by pointing Artifact at `site/day-one-circles.html`.)

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

## Working conventions

- **Run scripts by path, not as inline one-liners.** Write throwaway analysis to a file
  and run `python3 <path>`; set env vars like `MPLBACKEND` inside the script and do
  output filtering in Python rather than piping through `grep`. Inline commands with
  `VAR=x` prefixes or pipes miss the permission allowlist and cause approval prompts.
- Verify numeric claims by computing them before writing them down. Nearly every error
  in the source transcript was a plausible-sounding number nobody checked.
