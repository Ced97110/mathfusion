import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def ax2(ax, cx, cy, r):
    arrow(ax, (cx - r, cy), (cx + r, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - r), (cx, cy + r), 'fixe', lw=0.6)

ax2(ax, 22, 34, 17); ax2(ax, 66, 34, 17)
line(ax, [(6, 34), (38, 34)], 'sujet', lw=1.6)
line(ax, [(11, 23), (33, 45)], 'autre', lw=1.6)
line(ax, [(50, 34), (82, 34)], 'sujet', lw=1.6)
line(ax, [(66, 18), (66, 50)], 'resultat', lw=1.6)
line(ax, [(66, 38), (70, 38), (70, 34)], 'resultat', lw=0.8)
text(ax, 22, 56, 'somme directe', 'autre', 'm')
text(ax, 66, 56, 'somme orthogonale', 'resultat', 'm')
text(ax, 12, 40, r'$U_1$', 'sujet', 'm'); text(ax, 32, 47, r'$U_2$', 'autre', 'm')
text(ax, 76, 30, r'$U_1$', 'sujet', 'm'); text(ax, 71, 48, r'$U_2$', 'resultat', 'm')
text(ax, 22, 8, 'droites (1, 0) et (1, 1)', 'fixe', 's')
text(ax, 66, 8, 'à angle droit', 'resultat', 's')
save(fig, '72-044')
