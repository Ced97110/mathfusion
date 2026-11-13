import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'$(gN)(hN)=ghN$ : ligne de $g$ + ligne de $h$', 'encre', 's')
box(ax, 4, 38, 26, 22, 'sujet', fill=True); text(ax, 17, 55, 'ligne de 1', 'sujet', 's')
box(ax, 34, 38, 26, 22, 'autre', fill=True); text(ax, 47, 55, 'ligne de 2', 'autre', 's')
box(ax, 22, 4, 40, 18, 'resultat', fill=True); text(ax, 64, 13, 'ligne de 0', 'resultat', 's', ha='left')
pts = {'1': (10, 49), '4': (24, 49), '2': (40, 49), '5': (54, 49)}
for k, (x, y) in pts.items():
    col = 'sujet' if k in '14' else 'autre'
    disc(ax, x, y, 3.2, col, label=k)
text(ax, 32, 9.5, '3', 'resultat', 'm')
text(ax, 52, 9.5, '9', 'resultat', 'm')
arrow(ax, (12, 46), (30, 14), 'varie', lw=0.8)
arrow(ax, (38, 46), (31, 14), 'varie', lw=0.8)
arrow(ax, (25, 46), (50, 14), 'fixe', lw=0.8)
arrow(ax, (53, 46), (52, 14), 'fixe', lw=0.8)
text(ax, 72, 40, '1 + 2 = 3', 'varie', 's')
text(ax, 72, 31, '4 + 5 = 9', 'fixe', 's')
save(fig, '47-143')
