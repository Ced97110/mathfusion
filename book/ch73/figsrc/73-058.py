import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def panel(cx, cy, tr):
    line(ax, [(cx-17, cy), (cx+17, cy)], 'resultat', lw=1.3); line(ax, [(cx, cy-17), (cx, cy+17)], 'resultat', lw=1.3)
    return tr
cx, cy = 22, 34
panel(cx, cy, 0)
line(ax, [(cx-13, cy-13), (cx+13, cy+13)], 'resultat', lw=1.3)
text(ax, cx, 56, 'homothétie ×3', 'sujet', 's'); text(ax, cx, 8, 'toutes fixées', 'resultat', 's')
cx = 66
panel(cx, cy, 0)
line(ax, [(cx-13, cy-13), (cx+13, cy+13)], 'fixe', lw=1.0, dash=True)
line(ax, [(cx-17, cy-8.5), (cx+17, cy+8.5)], 'limite', lw=1.3)
text(ax, cx, 56, 'dilatation ×2', 'autre', 's'); text(ax, cx, 8, 'diagonale déplacée', 'limite', 's')
save(fig, '73-058')
