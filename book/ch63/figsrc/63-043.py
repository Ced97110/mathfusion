import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$H\subseteq G$', 'encre', 'xl', weight='bold')
box(ax, 3, 12, 82, 38, 'autre')
text(ax, 10, 45, r'$G$', 'autre', 'l', weight='bold')
box(ax, 8, 16, 36, 24, 'sujet')
text(ax, 14, 36, r'$H$', 'sujet', 'l', weight='bold')
for x, l, r in zip([17, 35, 56, 74], ['1', r'$\sigma$', r'$\tau$', r'$\sigma\tau$'], ['sujet', 'sujet', 'autre', 'autre']):
    disc(ax, x, 26, 5, r, label=l, size='s')
text(ax, 44, 5, r'même enchaînement que $G$', 'fixe', 's')
save(fig, '63-043')
