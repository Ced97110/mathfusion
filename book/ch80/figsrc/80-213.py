import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 2, 18, 30, 18, 'fixe', label='règles des\nanneaux', size='s')
box(ax, 38, 18, 20, 18, 'varie', label=r'$x^{2}=x$', size='m')
box(ax, 64, 18, 22, 18, 'resultat', label='algèbre de\nla logique', size='s')
text(ax, 35, 27, '+', 'encre', 'xl'); text(ax, 61, 27, '=', 'encre', 'xl')
text(ax, 17, 41, 'comme les nombres', 'fixe', 's')
text(ax, 48, 10, 'une seule règle en plus', 'varie', 's')
save(fig, '80-213')
