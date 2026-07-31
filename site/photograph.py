"""Photograph what board_program.py actually prints.

Not a redrawing of it -- the program is run, its stdout is captured with the
colour codes intact, and each character is placed in a fixed cell. So the figure
in the lesson is the output of the code printed beside it, and cannot drift.

Cells are twice as tall as they are wide, which is what a terminal does, so two
characters per lattice column comes out square. That is why the circles are round
here and were eggs when the aspect was guessed.
"""
import io
import pathlib
import re
import contextlib

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import board_program

BG   = '#0D1117'
PLAIN = '#2B333B'
RED   = '#FF5A4E'
OUT   = pathlib.Path(__file__).resolve().parent / 'plates'

ANSI = re.compile(r'\033\[(\d+)m')


def capture(r):
    """Run show(r) and return the lines, each as a list of (char, is_red)."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        board_program.show(r)
    lines = []
    for raw in buf.getvalue().splitlines():
        cells, red, i = [], False, 0
        while i < len(raw):
            m = ANSI.match(raw, i)
            if m:
                red = (m.group(1) == '31')
                i = m.end()
                continue
            cells.append((raw[i], red))
            i += 1
        lines.append(cells)
    return lines


def photograph(r, name, width_in=7.0):
    lines = capture(r)
    rows = len(lines)
    cols = max(len(l) for l in lines)

    # Fixed output width. A big grid rendered at its "natural" character size
    # produces a huge canvas with three-pixel dots, which reads as an empty box.
    # A terminal cell is about twice as tall as it is wide, so two characters
    # per lattice column comes out square.
    cell = width_in / cols
    fig_w, fig_h = width_in, rows * cell * 2
    fig = plt.figure(figsize=(fig_w, fig_h), facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(BG); ax.axis('off')
    ax.set_xlim(0, cols); ax.set_ylim(0, rows)

    xs_p, ys_p, xs_r, ys_r = [], [], [], []
    for row, cells in enumerate(lines):
        for col, (ch, is_red) in enumerate(cells):
            if ch == ' ':
                continue
            (xs_r if is_red else xs_p).append(col + .5)
            (ys_r if is_red else ys_p).append(rows - row - .5)
    # size the marks from the cell, so the ring stays legible at any radius:
    # red dots just touching, grid dots a third of that
    pt = cell * 72.0
    ax.scatter(xs_p, ys_p, s=(pt * .38) ** 2, marker='.', color=PLAIN, edgecolors='none')
    ax.scatter(xs_r, ys_r, s=(pt * 1.15) ** 2, marker='.', color=RED, edgecolors='none')

    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / name, facecolor=BG, dpi=140, bbox_inches='tight', pad_inches=.12)
    plt.close(fig)
    return rows, cols, len(xs_r)


if __name__ == '__main__':
    for r, name in ((12, 'p4_printed.png'), (60, 'p5_printed_big.png')):
        rows, cols, red = photograph(r, name)
        print(f'   show({r}) -> {rows} lines x {cols} characters, {red} red'
              f'   -> plates/{name}')
