import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
box(ax, 8, 36, 22, 22, 'sujet', label=r'$x$', size='xl', dash=True)
text(ax, 34, 51, 'boîte fermée,', 'sujet', 's', ha='left')
text(ax, 34, 45, 'poids pas encore mesuré', 'sujet', 's', ha='left')
text(ax, 34, 39, 'à chercher', 'sujet', 's', ha='left')
box(ax, 18, 10, 14, 12, 'sujet', label=r'$x$', dash=True)
text(ax, 38, 16, '+', 'encre', 'l')
box(ax, 44, 10, 12, 12, 'fixe', label='3')
brace(ax, 18, 56, 8, 'varie', label='se calcule avant la pesée', down=True)
save(fig, '16-014')
