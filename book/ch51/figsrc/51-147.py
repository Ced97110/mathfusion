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

fig, ax = canvas(70)
A = [[1, 2], [3, 4]]; B = [[5, 6], [7, 8]]
P = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert P == [[19, 22], [43, 50]]
y = 52
ca, ba = mat(ax, 14, y, A, 'sujet')
text(ax, 31, y, r'$\times$', 'encre', 'l')
cb, bb = mat(ax, 49, y, B, 'autre')
text(ax, 66, y, '=', 'encre', 'l')
cp, bp = mat(ax, 79, y, P, 'resultat', d=2)
# row 1 of A, column 1 of B, cell (1,1) of P
x0, _ = ca(0, 0); x1, _ = ca(0, 1)
ya = ca(0, 0)[1]
hl(ax, x0 - 3.2, x1 + 3.2, ya - 2.6, ya + 2.6)
xb, yb0 = cb(0, 0); _, yb1 = cb(1, 0)
hl(ax, xb - 3.2, xb + 3.2, yb1 - 2.6, yb0 + 2.6)
xp, yp = cp(0, 0)
hl(ax, xp - 3.2, xp + 3.2, yp - 2.6, yp + 2.6)
text(ax, 14, 63, 'ligne 1', 'varie', 's')
text(ax, 49, 63, 'colonne 1', 'varie', 's')
text(ax, 79, 63, 'case (1, 1)', 'varie', 's')
text(ax, 44, 33, r'$1\times5\;+\;2\times7$', 'sujet', 'l')
text(ax, 44, 24, r'$=\;5+14$', 'encre', 'l')
text(ax, 44, 15, r'$=\;19$', 'resultat', 'xl', weight='bold')
text(ax, 44, 5, 'produits deux à deux, puis somme', 'fixe', 's')
save(fig, '51-147')
