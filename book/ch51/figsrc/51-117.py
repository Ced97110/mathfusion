import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 81, r'$\mathbb{Z}/6$ : on entre tant que oui', 'encre', 'm')
steps = [('anneau : oui', 'on peut additionner et multiplier', 'resultat', 80),
         ('commutatif : oui', r'$2\times 3=3\times 2=0$', 'resultat', 68),
         ('intègre : non', r'$2\neq 0$, $3\neq 0$, $2\times 3=0$', 'limite', 56),
         ('corps', 'jamais atteint', 'fixe', 44)]
y = 56
arrow(ax, (44, 76.5), (44, 67.8), 'varie', lw=1.4); text(ax, 47, 72, 'on entre', 'varie', 's', ha='left')
for i, (a, b, role, wd) in enumerate(steps):
    box(ax, 44 - wd / 2, y, wd, 11, role, dash=(i == 3))
    text(ax, 44, y + 7.2, a, role, 'm', weight='bold'); text(ax, 44, y + 3, b, role, 's')
    if i < 2: arrow(ax, (44, y), (44, y - 5), 'varie')
    if i == 2:
        arrow(ax, (84, y + 5.5), (y and 72.8, y + 5.5), 'limite', lw=1.4)
        text(ax, 79, y + 9.5, 'arrêt', 'limite', 's', weight='bold')
    y -= 16
save(fig, '51-117')
