import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cx, cy, r = 26, 26, 17
disc(ax, cx, cy, r, 'fixe', fill=False)
arrow(ax, (cx, cy), (cx + r, cy), 'sujet', lw=1.4)
arrow(ax, (cx, cy), (cx, cy + r), 'resultat', lw=1.4)
arrow(ax, (cx + 9, cy), (cx, cy + 9), 'varie', curve=0.4)
text(ax, cx + r + 2, cy - 3.5, '(1, 0)', 'sujet', 's', ha='left')
text(ax, cx, cy + r + 4, '(0, 1)', 'resultat', 's')
text(ax, 66, 40, r'$O_n$', 'encre', 'xl')
text(ax, 66, 30, 'quart de tour', 'varie', 's')
text(ax, 66, 14, 'même longueur', 'fixe', 's')
save(fig, '75-062')
