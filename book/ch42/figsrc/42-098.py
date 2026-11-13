import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 4, 40, 58, 'fixe', fill=False)
box(ax, 46, 4, 40, 58, 'fixe', fill=False)
text(ax, 22, 57, 'existence', 'resultat', 'l', weight='bold')
text(ax, 66, 57, 'unicité', 'sujet', 'l', weight='bold')
text(ax, 22, 49, r'$2 + 3 = 5$', 'encre', 'm')
disc(ax, 22, 38, 5, 'resultat', label='2')
text(ax, 22, 28, 'un objet convient', 'resultat', 's')
box(ax, 8, 12, 28, 8, 'resultat', label='il existe', size='s')
arrow(ax, (22, 28 - 3), (22, 21), 'varie') if False else None
text(ax, 54, 49, r'$r + 3 = 5$', 'encre', 's'); text(ax, 78, 49, r'$s + 3 = 5$', 'encre', 's')
disc(ax, 54, 40, 4, 'sujet', label=r'$r$'); disc(ax, 78, 40, 4, 'sujet', label=r'$s$')
box(ax, 56, 12, 20, 8, 'resultat', label=r'$r = s$')
arrow(ax, (55, 35.5), (63, 21), 'varie'); arrow(ax, (77, 35.5), (69, 21), 'varie')
text(ax, 66, 27, 'même objet', 'varie', 's', ha='center') if False else None
text(ax, 66, 7.5, 'un seul objet', 'resultat', 's')
save(fig, '42-098')
