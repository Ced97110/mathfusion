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
SR = [[0, -2], [1, 0]]
x, y = (1.5, 0.5)
res = (SR[0][0] * x + SR[0][1] * y, SR[1][0] * x + SR[1][1] * y)
assert res == (-1.0, 1.5)
yy = 60
mat(ax, 14, yy, SR, 'sujet', d=2)
text(ax, 29, yy, r'$\times$', 'encre', 'l')
mat(ax, 43, yy, [['1,5'], ['0,5']], 'fixe', n=3, d=3)
text(ax, 58, yy, '=', 'encre', 'l')
mat(ax, 72, yy, [['-1'], ['1,5']], 'resultat', n=3, d=3)
text(ax, 44, 46, r'$0\times1{,}5+(-2)\times0{,}5=-1$', 'sujet', 's')
text(ax, 44, 40, r'$1\times1{,}5+0\times0{,}5=1{,}5$', 'sujet', 's')
u = 9.0; ox, oy = 30.0, 9.0
P = lambda a, b: (ox + a * u, oy + b * u)
arrow(ax, (ox - 14, oy), (ox + 26, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 3), (ox, oy + 24), 'fixe', lw=0.6)
arrow(ax, P(0, 0), P(1.5, 0.5), 'fixe', lw=1.2)
arrow(ax, P(0, 0), P(-1, 1.5), 'resultat', lw=1.4)
text(ax, P(1.5, 0.5)[0] + 4.5, P(1.5, 0.5)[1] + 0.5, r'$u$', 'fixe', 'm')
text(ax, P(-1, 1.5)[0] + 0.5, P(-1, 1.5)[1] + 3.5, r'flèche verte $SRu$', 'resultat', 's', ha='left')
save(fig, '51-157')
