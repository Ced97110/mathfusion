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

fig, ax = canvas(66)
# top: A -> -A
ca, ba = mat(ax, 14, 52, [[1, 2], [3, 4]], 'sujet')
cb, bb = mat(ax, 74, 52, [[-1, -2], [-3, -4]], 'varie', d=2)
arrow(ax, (ba[1] + 3, 52), (bb[0] - 3, 52), 'varie')
text(ax, 44, 57, 'chaque case change de signe', 'varie', 's')
text(ax, 14, 62, r'$A$', 'sujet', 'l')
text(ax, 74, 62, r'$-A$', 'varie', 'l')
# bottom: A + (-A) = 0
cy = 22
c1, b1 = mat(ax, 14, cy, [[1, 2], [3, 4]], 'sujet')
text(ax, 31, cy, '+', 'encre', 'l')
c2, b2 = mat(ax, 50, cy, [[-1, -2], [-3, -4]], 'varie', d=2)
text(ax, 68, cy, '=', 'encre', 'l')
c3, b3 = mat(ax, 79, cy, [[0, 0], [0, 0]], 'resultat')
text(ax, 44, 8, 'somme : 0 dans chaque case', 'resultat', 's')
save(fig, '51-145')
