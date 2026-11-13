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
fig, ax = canvas(56)
A = [[1, 1], [1, 0]]; B = [[0, 1], [1, 1]]
CY = 40
c1, c2, c3 = 14, 42, 74
# lignes et colonnes utilisées pour la case (1, 1)
hl(ax, c1 - 4, CY + SY - 2, 8, 4)
hl(ax, c2 - GX - 2, CY - 4, 4, 8)
x, y = cell(c3, CY, 0, 0); hl(ax, x - 2.2, y - 2.2, 4.4, 4.4)
mat(ax, c1, CY, A, 'sujet'); mat(ax, c2, CY, A, 'sujet'); mat(ax, c3, CY, B, 'resultat')
text(ax, 28, CY, r'$\times$', 'encre', 'l'); text(ax, 58, CY, '=', 'encre', 'l')
for cx, nm, role in ((c1, 'A', 'sujet'), (c2, 'A', 'sujet'), (c3, 'B', 'resultat')):
    text(ax, cx, CY - 9, f'${nm}$', role, 'l')
text(ax, 44, 20, 'case (1, 1), dans ℤ/2 :', 'varie', 'm')
text(ax, 44, 13, r'$1 \times 1 + 1 \times 1 = 2 = 0$', 'varie', 'l')
save(fig, '51-244')
