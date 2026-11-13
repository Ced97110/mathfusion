import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 22, 79, '(3) est maximal', 'resultat', 'm')
text(ax, 66, 79, "(6) n'est pas maximal", 'limite', 'm')
# gauche
box(ax, 13, 56, 18, 10, 'fixe', label='ℤ', size='m')
box(ax, 13, 30, 18, 10, 'sujet', label='(3)', size='m')
line(ax, [(22, 40), (22, 56)], 'resultat', lw=1.2)
text(ax, 22, 21, 'aucun idéal entre', 'resultat', 's')
text(ax, 22, 16, '(3) et ℤ', 'resultat', 's')
# droite
box(ax, 57, 56, 18, 10, 'fixe', label='ℤ', size='m')
box(ax, 57, 38, 18, 10, 'varie', label='(3)', size='m')
box(ax, 57, 20, 18, 10, 'autre', label='(6)', size='m')
line(ax, [(66, 48), (66, 56)], 'limite', lw=1.2)
line(ax, [(66, 30), (66, 38)], 'limite', lw=1.2)
text(ax, 66, 11, "(3) s'intercale", 'varie', 's')
save(fig, '56-111')
