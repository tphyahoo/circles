"""Is the implementation genuinely integer-only, or does it just look like it?

Two checks, because either alone is weak:

  STATIC  -- walk the syntax tree of lattice_circle.py and refuse anything that
             could produce a non-integer: true division, ** with a fractional
             exponent, float literals, math.sqrt, float().
  DYNAMIC -- run every function over a range of radii and assert that every
             number that comes out is an int, not merely int-valued.

Python's ints are arbitrary precision, which is the one thing it has genuinely
right for this: nothing silently overflows into a float or wraps around. The
discipline is not "avoid floats by being careful", it is checkable.
"""
import ast
import pathlib
import sys

TARGET = pathlib.Path(__file__).resolve().parent / 'lattice_circle.py'


# ------------------------------------------------------------------ static
class FloatHunter(ast.NodeVisitor):
    def __init__(self):
        self.found = []

    def _flag(self, node, what):
        self.found.append((getattr(node, 'lineno', 0), what))

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Div):
            self._flag(node, "true division '/' (use // or avoid)")
        if isinstance(node.op, ast.Pow):
            e = node.right
            if isinstance(e, ast.Constant) and not isinstance(e.value, int):
                self._flag(node, f"fractional power ** {e.value!r}")
        self.generic_visit(node)

    def visit_Constant(self, node):
        if isinstance(node.value, float):
            self._flag(node, f"float literal {node.value!r}")
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if node.attr in {'sqrt', 'hypot', 'dist', 'pi', 'e', 'tau'}:
            self._flag(node, f"math.{node.attr}")
        self.generic_visit(node)

    def visit_Name(self, node):
        if node.id in {'float', 'sqrt', 'hypot'}:
            self._flag(node, f"name {node.id!r}")
        self.generic_visit(node)


def _is_main_guard(node):
    return (isinstance(node, ast.If) and isinstance(node.test, ast.Compare)
            and isinstance(node.test.left, ast.Name) and node.test.left.id == '__name__')


def static_check(path):
    """The library and the demo are checked separately: the library must be clean,
    the demo is allowed to leave the integers to print a decimal."""
    tree = ast.parse(path.read_text(), str(path))
    lib  = ast.Module(body=[n for n in tree.body if not _is_main_guard(n)], type_ignores=[])
    demo = ast.Module(body=[n for n in tree.body if _is_main_guard(n)], type_ignores=[])
    a, b = FloatHunter(), FloatHunter()
    a.visit(lib); b.visit(demo)
    return a.found, b.found


# ----------------------------------------------------------------- dynamic
def every_number(obj):
    """Yield every scalar inside whatever came back."""
    if isinstance(obj, bool):
        return
    if isinstance(obj, (int, float)):
        yield obj
    elif isinstance(obj, (list, tuple, set, frozenset)):
        for v in obj:
            yield from every_number(v)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from every_number(k); yield from every_number(v)


def dynamic_check(radii):
    sys.path.insert(0, str(TARGET.parent))
    import lattice_circle as L
    bad = []
    for r in radii:
        results = {
            'draw':       L.draw(r),
            'count_dots': L.count_dots(r),
            'quadrance':  [L.quadrance((x, r)) for x in range(-r, r + 1)],
            'near_ring':  [L.near_ring((x, r), r) for x in range(-r, r + 1)],
            'mirrors':    L.mirrors((3, r)),
        }
        for name, res in results.items():
            for v in every_number(res):
                if not isinstance(v, int):
                    bad.append((r, name, type(v).__name__, v))
    return bad


if __name__ == '__main__':
    print(f'checking {TARGET.name}\n')

    found, demo = static_check(TARGET)
    print('STATIC  — the library (everything the algorithm actually uses):')
    if found:
        for line, what in found:
            print(f'   VIOLATION line {line}: {what}')
    else:
        print('   clean. no division, no fractional powers, no float literals, no sqrt.')

    print('\nSTATIC  — the demo block, which is allowed to leave the integers:')
    if demo:
        for line, what in demo:
            print(f'   line {line}: {what}   <- deliberate, this is where a count')
            print(f'{"":16}becomes a decimal for a human to read')
    else:
        print('   nothing.')

    radii = list(range(3, 60)) + [110, 257]
    bad = dynamic_check(radii)
    print(f'\nDYNAMIC — every number produced over {len(radii)} radii:')
    if bad:
        for r, name, ty, v in bad[:10]:
            print(f'   r={r} {name} produced a {ty}: {v!r}')
    else:
        print('   every value is an int. not int-valued — int.')

    print('\nnote: isqrt is the whole-number square root. It takes an int and')
    print('returns an int, and there is no float anywhere in between.')
    sys.exit(1 if (found or bad) else 0)
