import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 58, r'$-7p^{3}$', 'sujet', 'xl')
for i in range(7): box(ax, 4 + i * 12, 34, 11, 10, 'fixe', label='8', size='m')
brace(ax, 4, 87, 33, 'sujet', label='7 fois')
text(ax, 44, 49, r'pour $p=2$ : $p^{3}=8$', 'fixe', 's')
box(ax, 14, 6, 60, 10, 'resultat', label=r'$7\times8=56$, donc $-56$', size='m')
save(fig, '15-077')
