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
fig, ax = canvas(80)
YS = (58, 38, 18)            # bas de chaque prémisse
for y in YS:
    box(ax, 2, y, 52, 16, 'sujet')
    arrow(ax, (54, y + 8), (60, y + 8), 'resultat', lw=1.2)
box(ax, 60, 18, 26, 56, 'resultat')
text(ax, 73, 68, 'corps', 'resultat', 'l', weight='bold')
text(ax, 73, 52, r'$A$ : inverse $B$', 'resultat', 'm')
text(ax, 73, 44, r'$I$ : inverse $I$', 'resultat', 'm')
# prémisse 1 : commutatif
text(ax, 5, 66, 'commutatif', 'sujet', 'm', ha='left')
text(ax, 40, 66, r'$AB = BA = I$', 'sujet', 'm')
# prémisse 2 : intègre (table des 9 produits non nuls, sans 0)
text(ax, 5, 46, 'intègre', 'sujet', 'm', ha='left')
for i in range(3):
    for j in range(3):
        box(ax, 40 + 4.2 * j, 40 + 4.2 * (2 - i), 3.8, 3.8, 'resultat', r=0.4, lw=0.5)
text(ax, 28, 46, r'produits $\neq 0$', 'sujet', 's')
# prémisse 3 : fini (4 éléments)
text(ax, 5, 26, 'fini', 'sujet', 'm', ha='left')
for k, nm in enumerate(['0', 'I', 'A', 'B']):
    box(ax, 22 + 7.6 * k, 22.5, 7, 7, 'fixe', r=0.5, lw=0.6, label=nm if nm == '0' else f'${nm}$', size='s')
save(fig, '51-248')
