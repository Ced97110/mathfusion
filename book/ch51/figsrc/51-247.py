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
fig, ax = canvas(70)
names = ['I', 'A', 'B']
# table de multiplication de F privé de 0 (le produit de 2 éléments est lu à l'intersection)
PROD = {('I', 'I'): 'I', ('I', 'A'): 'A', ('I', 'B'): 'B', ('A', 'I'): 'A', ('A', 'A'): 'B',
        ('A', 'B'): 'I', ('B', 'I'): 'B', ('B', 'A'): 'I', ('B', 'B'): 'A'}
CW, CH = 14.0, 10.0
X0, Y0 = 30.0, 52.0          # coin haut-gauche des 9 cases
for j, n in enumerate(names):
    text(ax, X0 + CW * (j + 0.5), Y0 + 5, f'${n}$', 'sujet', 'm')
t = text(ax, X0 - 7, Y0 - CH * 1.5, '\n'.join(f'${n}$' for n in names), 'sujet', 'm')
t.set_linespacing(4.66)
for i, a in enumerate(names):
    for j, b in enumerate(names):
        box(ax, X0 + CW * j + 0.6, Y0 - CH * (i + 1) + 0.6, CW - 1.2, CH - 1.2, 'resultat', r=0.6,
            label=f'${PROD[(a, b)]}$')
text(ax, 44, 12, 'aucun des 9 produits n’est 0', 'resultat', 'm')
save(fig, '51-247')
