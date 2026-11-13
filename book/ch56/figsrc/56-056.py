import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, 'deux écritures du même nombre 4', 'encre', 'm')
# première écriture : 2 × 2
box(ax, 2, 38, 16, 12, 'sujet', label='2', size='m')
text(ax, 22, 44, '×', 'encre', 'm')
box(ax, 26, 38, 16, 12, 'sujet', label='2', size='m')
text(ax, 47, 44, '=', 'encre', 'm')
box(ax, 52, 38, 16, 12, 'resultat', label='4', size='m')
# seconde écriture
box(ax, 2, 10, 30, 12, 'autre', label=r'$1-\sqrt{3}\,i$', size='s')
text(ax, 35, 16, '×', 'encre', 'm')
box(ax, 38, 10, 30, 12, 'autre', label=r'$1+\sqrt{3}\,i$', size='s')
text(ax, 71, 16, '=', 'encre', 'm')
box(ax, 74, 10, 12, 12, 'resultat', label='4', size='m')
text(ax, 44, 2.5, '1 − (−3) = 1 + 3 = 4', 'fixe', 's')
save(fig, '56-056')
