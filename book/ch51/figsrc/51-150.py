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

fig, ax = canvas(80)
text(ax, 44, 77, 'on applique S, puis R', 'fixe', 's')
bw, bh, by = 22, 11, 56
xs = (2, 33, 64)
labs = (r'$(x,\ y)$', r'$(2x,\ y)$', r'$(-y,\ 2x)$')
roles = ('fixe', 'fixe', 'resultat')
for x, l, r in zip(xs, labs, roles):
    box(ax, x, by, bw, bh, r, label=l, size='m')
arrow(ax, (xs[0] + bw + 0.5, by + bh / 2), (xs[1] - 0.5, by + bh / 2), 'sujet')
arrow(ax, (xs[1] + bw + 0.5, by + bh / 2), (xs[2] - 0.5, by + bh / 2), 'autre')
text(ax, (xs[0] + bw + xs[1]) / 2, by + bh / 2 + 3.2, r'$S$', 'sujet', 'l')
text(ax, (xs[1] + bw + xs[2]) / 2, by + bh / 2 + 3.2, r'$R$', 'autre', 'l')
# direct arrow below the boxes: the product
arrow(ax, (xs[0] + bw / 2, by - 1), (xs[2] + bw / 2, by - 1), 'resultat', curve=0.28, lw=1.2)
text(ax, 44, 41, 'd’un seul coup : $RS$', 'resultat', 'm')
# matrices
S = [[2, 0], [0, 1]]; R = [[0, -1], [1, 0]]
RS = [[sum(R[i][k] * S[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert RS == [[0, -1], [2, 0]]
y = 22
text(ax, 1, y, r'$S=$', 'sujet', 'm', ha='left')
mat(ax, 15, y, S, 'sujet')
text(ax, 27, y, r'$R=$', 'autre', 'm', ha='left')
mat(ax, 45, y, R, 'autre', d=2)
text(ax, 54, y, r'$RS=$', 'resultat', 'm', ha='left')
mat(ax, 74, y, RS, 'resultat', d=2)
save(fig, '51-150')
