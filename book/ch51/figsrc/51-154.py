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

fig, ax = canvas(58)
u = 13.0
def plane(cx, cy):
    arrow(ax, (cx - 16, cy), (cx + 17, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - 4), (cx, cy + 19), 'fixe', lw=0.6)
    return lambda x, y: (cx + x * u, cy + y * u)
L = plane(22, 34); Rr = plane(66, 34)
text(ax, 22, 56, 'départ', 'fixe', 's')
text(ax, 66, 56, 'après le quart de tour', 'fixe', 's')
arrow(ax, L(0, 0), L(1, 0), 'sujet', lw=1.3)
arrow(ax, L(0, 0), L(0, 1), 'autre', lw=1.3)
text(ax, L(1, 0)[0] + 1.5, L(1, 0)[1] - 3.6, r'$(1\ ;\ 0)$', 'sujet', 's', ha='center')
text(ax, L(0, 1)[0] + 9, L(0, 1)[1], r'$(0\ ;\ 1)$', 'autre', 's')
arrow(ax, Rr(0, 0), Rr(0, 1), 'sujet', lw=1.3)
arrow(ax, Rr(0, 0), Rr(-1, 0), 'autre', lw=1.3)
text(ax, Rr(0, 1)[0] + 9, Rr(0, 1)[1], r'$(0\ ;\ 1)$', 'sujet', 's')
text(ax, Rr(-1, 0)[0], Rr(-1, 0)[1] - 3.6, r'$(-1\ ;\ 0)$', 'autre', 's')
arrow(ax, Rr(0.5, 0.04), Rr(0.04, 0.5), 'varie', curve=0.45, lw=1.0)
text(ax, Rr(0.5, 0.5)[0] + 1.5, Rr(0.5, 0.5)[1] - 1.5, 'quart\nde tour', 'varie', 's', ha='left')
# matrix with coloured columns
my = 11
mat(ax, 44, my, [[0, -1], [1, 0]], 'fixe', col_roles=('sujet', 'autre'), d=2)
text(ax, 29, my, '1re colonne :\nimage de (1 ; 0)', 'sujet', 's', ha='right')
text(ax, 59, my, '2e colonne :\nimage de (0 ; 1)', 'autre', 's', ha='left')
save(fig, '51-154')
