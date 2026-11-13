import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
GX, SY = 2.08, 1.78
def mat(ax, cx, cy, M, role='sujet'):
    t = text(ax, cx, cy, f'{M[0][0]}   {M[0][1]}\n{M[1][0]}   {M[1][1]}', role, 'm'); t.set_linespacing(1.5)
    for s in (-1, 1):
        x = cx + s * 4.6
        line(ax, [(x - s * 1.2, cy + 4.4), (x, cy + 4.4), (x, cy - 4.4), (x - s * 1.2, cy - 4.4)], role, lw=0.8)
def cell(cx, cy, r, c): return (cx + (c - 0.5) * 2 * GX, cy + (0.5 - r) * 2 * SY)
def hl(ax, x, y, w, h, role='varie'):
    ax.add_patch(Rectangle((x, y), w, h, fc=FILL[role], ec=COL[role], lw=0.6, zorder=1))
fig, ax = canvas(64)
OX, OY, U = 12.0, 14.0, 14.0
px = lambda a: OX + a * U
py = lambda b: OY + b * U
arrow(ax, (OX, OY), (px(3) + 8, OY), 'fixe', lw=0.9)
arrow(ax, (OX, OY), (OX, py(2) + 8), 'fixe', lw=0.9)
text(ax, px(3) + 12, OY, '$a$', 'fixe', 'm'); text(ax, OX, py(2) + 12, '$b$', 'fixe', 'm')
tx = {1: 'autre', 2: 'fixe', 3: 'sujet'}; ty = {1: 'sujet', 2: 'autre'}
for a, role in tx.items():
    line(ax, [(px(a), OY - 1), (px(a), OY + 1)], 'fixe'); text(ax, px(a), OY - 4, str(a), role, 's')
for b, role in ty.items():
    line(ax, [(OX - 1, py(b)), (OX + 1, py(b))], 'fixe'); text(ax, OX - 4.5, py(b), str(b), role, 's')
for (a, b, role, lab, nrm, ny) in ((3, 1, 'sujet', r'$3 + i$', r'$N = 9 + 1 = 10$', 22), (1, 2, 'autre', r'$1 + 2i$', r'$N = 1 + 4 = 5$', 43)):
    line(ax, [(px(a), OY), (px(a), py(b))], role, dash=True, lw=0.7)
    line(ax, [(OX, py(b)), (px(a), py(b))], role, dash=True, lw=0.7)
    line(ax, [(OX, OY), (px(a), py(b))], role, lw=1.3)
    disc(ax, px(a), py(b), 1.3, role)
    text(ax, px(a) + 2.5, py(b) + 3.2, lab, role, 'm', ha='left')
    text(ax, 86, ny, nrm, role, 'm', ha='right')
text(ax, 44, 3.5, r'$N$ : carré de la distance', 'encre', 'm')
save(fig, '51-255')
