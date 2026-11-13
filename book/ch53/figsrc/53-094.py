import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ya = 52
f = numberline(ax, 6, 78, ya, 0, 54, step=1, labels=False, arrow_right=False, tick=0.8)
brace(ax, f(0), f(54), ya + 3, 'fixe', label=r'$0\leq m<n=55$', down=False)
for v in (0, 54):
    text(ax, f(v), ya - 3.5, str(v), 'fixe', 's')
for v in (8, 12, 34):
    disc(ax, f(v), ya, 1.4, 'resultat')
text(ax, f(8), ya - 3.5, '8', 'resultat', 's')
box(ax, f(12) - 6, 28, 12, 8, 'resultat', label='12')
box(ax, f(34) - 6, 28, 12, 8, 'resultat', label='34')
arrow(ax, (f(12), 36.5), (f(12), ya - 1.8), 'resultat')
arrow(ax, (f(34), 36.5), (f(34), ya - 1.8), 'resultat')
box(ax, 30, 4, 28, 10, 'limite', label='3 412')
text(ax, 72, 9, 'trop grand', 'limite', 's')
arrow(ax, (38, 14.5), (f(12) + 2, 27.5), 'varie')
arrow(ax, (50, 14.5), (f(34) - 2, 27.5), 'varie')
text(ax, 44, 21, 'coupé', 'varie', 's')
save(fig, '53-094')
