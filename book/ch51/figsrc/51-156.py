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

fig, ax = canvas(74)
S = [[2, 0], [0, 1]]; R = [[0, -1], [1, 0]]
SR = [[sum(S[i][k] * R[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert SR == [[0, -2], [1, 0]]
y = 58
cs, bs = mat(ax, 14, y, S, 'sujet')
text(ax, 30, y, r'$\times$', 'encre', 'l')
cr, br = mat(ax, 47, y, R, 'autre', d=2)
text(ax, 63, y, '=', 'encre', 'l')
cp, bp = mat(ax, 78, y, SR, 'resultat', d=2)
x0 = cs(0, 0)[0]; x1 = cs(0, 1)[0]; ya = cs(0, 0)[1]
hl(ax, x0 - 3.2, x1 + 3.2, ya - 2.6, ya + 2.6)
xc = cr(0, 0)[0] + 0.0; yt = cr(0, 0)[1]; yb = cr(1, 0)[1]
hl(ax, xc - 3.2, xc + 3.2, yb - 2.6, yt + 2.6)
xp, yp = cp(0, 0)
hl(ax, xp - 3.2, xp + 3.2, yp - 2.6, yp + 2.6)
text(ax, 44, 44, r'case en haut à gauche : $2\times0+0\times1=0$', 'varie', 's')
text(ax, 44, 38, r'les quatre cases : $0,\ -2,\ 1,\ 0$', 'resultat', 's')
# check on u
y2 = 17
u = ['1,5', '0,5']; v = ['-1', '1,5']
text(ax, 2, 28, 'vérification sur le point u :', 'fixe', 's', ha='left')
mat(ax, 18, y2, SR, 'resultat', d=2)
mat(ax, 38, y2, [u[0:1], u[1:2]], 'fixe', n=3, d=3)
text(ax, 50, y2, '=', 'encre', 'l')
mat(ax, 62, y2, [v[0:1], v[1:2]], 'resultat', n=3, d=3)
text(ax, 44, 4, 'le résultat est la flèche verte', 'resultat', 's')
save(fig, '51-156')
