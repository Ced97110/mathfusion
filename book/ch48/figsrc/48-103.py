import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 2, 46, 40, 12, 'sujet', label=r'$\langle 4\rangle$ : 0, 4, 8', size='s')
box(ax, 46, 46, 40, 12, 'autre', label=r'$\langle 2\rangle$ : 0, 2, …, 10', size='s')
text(ax, 44, 64, 'deux sous-groupes différents', 'limite', 's')
box(ax, 4, 6, 80, 26, 'resultat')
text(ax, 44, 26, r'même image dans $G/K$', 'resultat', 's')
for x, s in [(20, '{0, 6}'), (44, '{2, 8}'), (68, '{4, 10}')]:
    box(ax, x - 10, 9, 20, 9, 'resultat', label=s, size='s')
arrow(ax, (22, 45.5), (30, 32.5), 'varie'); arrow(ax, (66, 45.5), (58, 32.5), 'varie')
save(fig, '48-103')
