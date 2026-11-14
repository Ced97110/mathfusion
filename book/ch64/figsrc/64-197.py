import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
assert 2 * 2 == 4
text(ax, 44, 67, r'$x^5-1=0$ : $G$ a 4 éléments', 'sujet', 'm')
box(ax, 4, 46, 30, 12, 'sujet', label=r'$\mathbb{Q}(z)$')
box(ax, 4, 26, 30, 12, 'sujet', label='étage 1', size='s', dash=True)
box(ax, 4, 6, 30, 12, 'sujet', label=r'$\mathbb{Q}$')
for ya, yb in ((19, 25), (39, 45)):
    arrow(ax, (14, ya), (14, yb), 'varie')
    text(ax, 18, (ya + yb) / 2, 'racine carrée', 'varie', 's', ha='left')
box(ax, 52, 46, 34, 12, 'resultat', label=r'$4=2\times2$')
text(ax, 69, 40, 'deux étages\nd’exposant 2', 'resultat', 's', va='top')
text(ax, 69, 17, r'$n$ : pour quelles\nvaleurs ?'.replace('\\n', '\n'), 'autre', 'm')
save(fig, '64-197')
