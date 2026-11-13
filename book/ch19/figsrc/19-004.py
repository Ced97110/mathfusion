import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 3, 36, 40, 14, 'fixe'); text(ax, 23, 46, 'le prix total', 'encre', 'm'); text(ax, 23, 40.5, 'à payer en euros', 'encre', 'm')
arrow(ax, (44, 43), (62, 43), 'varie'); text(ax, 53, 47, 'un seul signe', 'varie', 's')
box(ax, 63, 35, 22, 16, 'sujet', label=r'$y$', size='xl')
text(ax, 22, 27, '3 cahiers', 'fixe', 's'); text(ax, 22, 8, '5 cahiers', 'fixe', 's')
text(ax, 62, 27, r'$y$ = 7', 'sujet', 'l'); text(ax, 62, 8, r'$y$ = 11', 'sujet', 'l')
save(fig, '19-004')
