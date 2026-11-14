import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def panel(x, titre, role):
    text(ax, x + 18, 74, titre, role, 'm', weight='bold')
    box(ax, x, 60, 36, 9, 'varie', label='coefficients 2 et 1', size='s')
    box(ax, x, 40, 36, 15, 'fixe')
    text(ax, x + 18, 50, r'$2\ \ -1$', 'encre', 's'); text(ax, x + 18, 44, r'$1\ \ \ \ \ 2$', 'encre', 's')
    box(ax, x, 27, 36, 9, 'resultat', label='trace 4', size='s')
    box(ax, x, 14, 36, 9, 'resultat', label='norme 5', size='s')
panel(2, 'sur les réels', 'sujet'); panel(50, 'sur les complexes', 'autre')
for y in (64.5, 47.5, 31.5, 18.5): text(ax, 44, y, '=', 'resultat', 'l')
save(fig, '77-130')
