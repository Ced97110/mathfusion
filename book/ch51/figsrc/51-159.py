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

fig, ax = canvas(86)
text(ax, 44, 82, 'trois matrices 2 × 2 à ne pas confondre', 'fixe', 's')
xs = (15, 44, 73); y = 62
box(ax, 44 - 13.5, y - 11, 27, 22, 'sujet')
mat(ax, xs[0], y, [[0, 0], [0, 0]], 'fixe')
mat(ax, xs[1], y, [[1, 0], [0, 1]], 'sujet')
mat(ax, xs[2], y, [[r'a', 0], [0, r'b']], 'autre')
text(ax, xs[0], 45, 'nulle', 'fixe', 's')
text(ax, xs[0], 40.5, 'neutre de +', 'fixe', 's')
text(ax, xs[1], 45, 'unité', 'sujet', 's', weight='bold')
text(ax, xs[1], 40.5, 'neutre de ×', 'sujet', 's')
text(ax, xs[2], 45, 'diagonale', 'autre', 's')
text(ax, xs[2], 40.5, 'autres nombres', 'autre', 's')
# A x I = A
A = [[3, 4], [5, 6]]
y2 = 17
mat(ax, 14, y2, A, 'fixe')
text(ax, 29, y2, r'$\times$', 'encre', 'l')
mat(ax, 44, y2, [[1, 0], [0, 1]], 'sujet')
text(ax, 59, y2, '=', 'encre', 'l')
mat(ax, 74, y2, A, 'resultat')
text(ax, 44, 4, 'la matrice reste la même', 'resultat', 's')
save(fig, '51-159')
