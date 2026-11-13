import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 23, 77, 'le café', 'sujet', 'm'); text(ax, 65, 77, 'avec 3y', 'autre', 'm')
cols = [(3, 'sujet', [r'$x+y=5$', r'$y=5-x$']), (45, 'autre', [r'$2x+3y=12$', r'$y=4-\frac{2x}{3}$'])]
for x0, role, labs in cols:
    box(ax, x0, 52, 40, 11, role, label=labs[0]); box(ax, x0, 30, 40, 13, role, label=labs[1])
    arrow(ax, (x0 + 20, 52), (x0 + 20, 43), 'varie'); text(ax, x0 + 22, 47.5, 'isoler y', 'varie', 's', ha='left')
box(ax, 3, 8, 40, 11, 'resultat', label=r'$x=3,\ y=2$'); arrow(ax, (23, 30), (23, 19), 'varie')
box(ax, 45, 8, 40, 11, 'autre', fill=False, dash=True, label='une fraction', size='s'); arrow(ax, (65, 30), (65, 19), 'varie')
save(fig, '24-038')
