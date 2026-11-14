import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

FS = ' '  # figure space: same width as a digit

def mat(ax, cx, cy, rows, role='sujet', size='m', n=2, sep=2, ls=2.2, col_roles=None, d=1):
    """Matrix drawn as aligned text with brackets. Returns (cell(i, j) -> (x, y), (x0, x1, y0, y1))."""
    fs = SIZE[size] * 25.4 / 72
    cw = 0.636 * fs
    px = (n + sep) * cw
    py = 1.05 * fs * (0.767 * ls + 0.194)
    nr, nc = len(rows), len(rows[0])
    cell = lambda i, j: (cx + (j - (nc - 1) / 2) * px, cy + ((nr - 1) / 2 - i) * py)
    fmt = lambda v: str(v).replace('-', '−').rjust(n, FS)
    if col_roles is None:
        t = text(ax, cx - (n - d) * cw / 2, cy, '\n'.join((FS * sep).join(fmt(v) for v in r) for r in rows), role, size)
        t.set_linespacing(ls)
    else:
        for j in range(nc):
            t = text(ax, cell(0, j)[0] - (n - d) * cw / 2, cy, '\n'.join(fmt(r[j]) for r in rows), col_roles[j], size)
            t.set_linespacing(ls)
    w = (nc - 1) * px + n * cw + 2.4
    h = nr * py + 0.6
    x0, x1, y0, y1 = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    for xs, d in ((x0, 1.2), (x1, -1.2)):
        line(ax, [(xs + d, y1), (xs, y1), (xs, y0), (xs + d, y0)], role, lw=0.9)
    return cell, (x0, x1, y0, y1)

def hl(ax, x0, x1, y0, y1, role='varie'):
    """Dashed highlight frame."""
    box(ax, x0, y0, x1 - x0, y1 - y0, role, fill=False, lw=1.0, r=0.6, dash=True)

fig, ax = canvas(62)
A = [[1, 2], [3, 4]]; B = [[5, 6], [7, 8]]
S = [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]   # [[6, 8], [10, 12]]
xs = (13, 45, 76)
def line_of(y, first, second, r1, r2):
    c1, b1 = mat(ax, xs[0], y, first, r1)
    text(ax, 29, y, '+', 'encre', 'l')
    c2, b2 = mat(ax, xs[1] - 4, y, second, r2)
    text(ax, 61, y, '=', 'encre', 'l')
    c3, b3 = mat(ax, xs[2] + 2, y, S, 'resultat', n=2, d=2)
    return c1, c2, c3
y1, y2 = 47, 21
c1, c2, c3 = line_of(y1, A, B, 'sujet', 'autre')
d1, d2, d3 = line_of(y2, B, A, 'autre', 'sujet')
# highlight the top-right cell in each row (2 and 6, then their sum 8)
for (ca, cb, cc) in ((c1, c2, c3), (d1, d2, d3)):
    for c in (ca, cb, cc):
        x, y = c(0, 1)
        hl(ax, x - 3.2, x + 3.2, y - 2.6, y + 2.6)
text(ax, 44, 8, r'$2+6=6+2$ : même résultat', 'resultat', 's')
text(ax, 44, 57, 'addition case par case', 'fixe', 's')
save(fig, '51-146')
