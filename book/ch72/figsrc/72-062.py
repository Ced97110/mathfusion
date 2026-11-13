import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
f = numberline(ax, 8, 70, 38, -2, 3, labels=True, arrow_right=True)
brace(ax, f(-1), f(1), 50, 'fixe', down=False, label='orthogonales : −1 ou 1')
text(ax, 44, 60, r'valeur du déterminant', 'fixe', 's')
for v, r, t, y in ((-1, 'sujet', 'impropre', 24), (1, 'fixe', 'rotation', 24), (2, 'limite', r'$(2a\ ;\ b)$', 17)):
    disc(ax, f(v), 38, 2.4, r)
    text(ax, f(v), y, t, r, 's', weight='bold' if v == -1 else 'normal')
    line(ax, [(f(v), 29.8), (f(v), y + 3)], r, lw=0.6, dash=True)
text(ax, f(2), 11, 'déterminant 2', 'limite', 's')
text(ax, f(2), 5, 'ne garde pas la mesure', 'limite', 's')
save(fig, '72-062')
