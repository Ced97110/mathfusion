import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 32, 58, 24, 14, 'sujet', label='$12$', size='l')
for i, (x, v) in enumerate(((8, 2), (34, 2), (60, 3))):
    box(ax, x, 30, 20, 14, 'resultat', label=f'${v}$', size='l')
    arrow(ax, (44 + (i - 1) * 6, 58), (x + 10, 45), 'resultat', lw=0.8)
text(ax, 44, 22, 'une seule liste de premiers', 'resultat', 's')
box(ax, 3, 3, 38, 12, 'resultat', label='$\\mathbb{Z}$ : oui', size='m')
box(ax, 47, 3, 38, 12, 'autre', label='Gauss : à voir', size='m', dash=True)
save(fig, '51-278')
