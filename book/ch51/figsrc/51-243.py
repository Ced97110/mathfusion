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
fig, ax = canvas(72)
# left : 16 tableaux, 4 choisis
text(ax, 20, 67, '16 tableaux', 'fixe', 'm')
chosen = {(0, 1), (1, 3), (2, 0), (3, 2)}
for r in range(4):
    for c in range(4):
        role = 'sujet' if (r, c) in chosen else 'fixe'
        box(ax, 4 + 8 * c, 52 - 8 * r - 0, 7, 7, role, r=0.6)
text(ax, 20, 22, r'$F$ : 4 parmi 16', 'sujet', 'm')
# right top : Z/4
text(ax, 64, 67, 'ℤ/4 : 4 éléments', 'autre', 'm')
for k in range(4):
    box(ax, 47 + 9 * k, 54, 8, 8, 'autre', label=str(k))
text(ax, 64, 49, r'$2 \times 2 = 0$ : diviseur de zéro', 'limite', 'm')
# right bottom : F
text(ax, 64, 38, r'$F$ : 4 éléments', 'sujet', 'm')
for k, nm in enumerate(['0', 'I', 'A', 'B']):
    box(ax, 47 + 9 * k, 25, 8, 8, 'sujet', label=nm if nm == '0' else f'${nm}$')
text(ax, 64, 20, 'produits non nuls : jamais 0', 'resultat', 'm')
save(fig, '51-243')
