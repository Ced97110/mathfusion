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
Rq = [[0, -1], [1, 0]]
# top: the two candidate products of Rq by Rq
text(ax, 44, 76, r'quart de tour $\times$ quart de tour', 'fixe', 's')
text(ax, 22, 68, 'ligne-colonne', 'resultat', 's')
text(ax, 66, 68, 'case par case', 'limite', 's')
mat(ax, 22, 57, [[-1, 0], [0, -1]], 'resultat', d=2)
mat(ax, 66, 57, [[0, 1], [1, 0]], 'limite')
# bottom: where the point (1 ; 0) goes
u = 9.0
def plane(cx, cy):
    arrow(ax, (cx - 15, cy), (cx + 16, cy), 'fixe', lw=0.7)
    arrow(ax, (cx, cy - 12), (cx, cy + 15), 'fixe', lw=0.7)
    return lambda x, y: (cx + x * u, cy + y * u)
P1 = plane(22, 26); P2 = plane(66, 26)
# left: two quarter turns -> (-1 ; 0)
disc(ax, *P1(1, 0), 1.5, 'fixe')
disc(ax, *P1(-1, 0), 1.5, 'resultat')
ax.add_patch(matplotlib.patches.Arc(P1(0, 0), 2 * u, 2 * u, theta1=2, theta2=176, ec=COL['resultat'], lw=1.0, zorder=3))
arrow(ax, (P1(0, 0)[0] - u * 0.99, P1(0, 0)[1] + 0.9), P1(-1, 0), 'resultat', lw=1.0)
text(ax, P1(1, 0)[0] + 1, P1(1, 0)[1] - 4.5, r'$(1\ ;\ 0)$', 'fixe', 's')
text(ax, P1(-1, 0)[0] - 1, P1(-1, 0)[1] - 4.5, r'$(-1\ ;\ 0)$', 'resultat', 's')
text(ax, 22, 8, 'demi-tour : le point passe en face', 'resultat', 's')
# right: coordinates swapped -> (0 ; 1)
disc(ax, *P2(1, 0), 1.5, 'fixe')
disc(ax, *P2(-1, 0), 1.5, 'resultat', fill=False)
disc(ax, *P2(0, 1), 1.5, 'limite')
arrow(ax, (P2(1, 0)[0] - 1, P2(1, 0)[1] + 1), (P2(0, 1)[0] + 1, P2(0, 1)[1] - 1), 'limite', lw=1.0)
text(ax, P2(1, 0)[0] + 1, P2(1, 0)[1] - 4.5, r'$(1\ ;\ 0)$', 'fixe', 's')
text(ax, P2(0, 1)[0] + 12, P2(0, 1)[1] + 1.5, r'$(0\ ;\ 1)$', 'limite', 's')
text(ax, P2(-1, 0)[0], P2(-1, 0)[1] - 4.5, 'attendu', 'resultat', 's')
text(ax, 66, 8, 'les coordonnées s’échangent', 'limite', 's')
save(fig, '51-149')
