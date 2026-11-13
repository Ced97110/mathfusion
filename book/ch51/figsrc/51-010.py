import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 2, 44, 84, 10, 'fixe', label='mêmes huit règles dans les deux mondes', size='s')
for x, nom, role, l1, l2, v in [(2, 'entiers', 'resultat', r'$2\times a=2\times b$', r'donne $a=b$', 'simplifier : oui'),
                               (46, 'cadran à 4 h', 'limite', r'$2\times1=2=2\times3$', r'mais $1\neq3$', 'simplifier : non')]:
    xc = x + 20
    arrow(ax, (xc, 44), (xc, 39.5), 'fixe')
    text(ax, xc, 36, nom, 'encre', 'm', weight='bold')
    box(ax, x, 14, 40, 18, role)
    text(ax, xc, 26, l1, role, 's')
    text(ax, xc, 19, l2, role, 's')
    text(ax, xc, 8, v, role, 'm', weight='bold')
save(fig, '51-010')
