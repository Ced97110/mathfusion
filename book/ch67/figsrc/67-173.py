import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def mulx(v):
    a0, a1, a2, a3 = v
    return [a3, a0 ^ a3, a1, a2]
p = [[1, 0, 0, 0]]
for _ in range(15):
    p.append(mulx(p[-1]))
b8, b9 = p[8], p[9]
assert b8 == [1, 0, 1, 0] and b9 == [0, 1, 0, 1]
s = [x ^ y for x, y in zip(b8, b9)]
assert s == [1, 1, 1, 1] and (8 + 9) % 15 == 2
def row(y, bits, role):
    for c in range(4):
        x = 14 + c * 8.5
        if bits[c]:
            ax.add_patch(Rectangle((x, y), 7.5, 6, ec=COL[role], fc=COL[role], lw=0.5, zorder=2))
        else:
            ax.add_patch(Rectangle((x, y), 7.5, 6, ec=COL['fixe'], fc=FILL['fixe'], lw=0.5, zorder=2))
text(ax, 25, 60, 'somme : bits', 'sujet')
row(46, b8, 'sujet'); text(ax, 12, 49, r'$\alpha^8$', 'sujet', ha='right')
row(38, b9, 'sujet'); text(ax, 12, 41, r'$\alpha^9$', 'sujet', ha='right')
line(ax, [(14, 35), (47, 35)], 'fixe')
row(27, s, 'resultat'); text(ax, 12, 30, 'somme', 'resultat', 's', ha='right')
text(ax, 30, 20, 'colonne par colonne', 'fixe', 's')
text(ax, 30, 14, 'bleu = 1', 'sujet', 's')
text(ax, 68, 60, 'produit : exposants', 'autre')
box(ax, 52, 44, 33, 10, 'autre', label=r'$8+9=17$')
arrow(ax, (68.5, 44), (68.5, 38.8), 'varie')
box(ax, 52, 28, 33, 10, 'autre', label=r'$17-15=2$')
arrow(ax, (68.5, 28), (68.5, 22.8), 'varie')
box(ax, 52, 12, 33, 10, 'resultat', label=r'$\alpha^8\alpha^9=\alpha^2$')
save(fig, '67-173')
