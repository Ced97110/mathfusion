import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
u, x0 = 70 / 6100, 9
fig, ax = canvas(56)
box(ax, x0, 40, 1600*u, 9, 'fixe', label='$a^2$\n1 600', size='s', r=0.5)
box(ax, x0 + 1600*u, 40, 4500*u, 9, 'autre', label='2bc cos A = 4 500', size='s', r=0.5)
brace(ax, x0, x0 + 6100*u, 49, 'sujet', label='b² + c² = 6 100', down=False)
box(ax, x0, 14, 6000*u, 9, 'fixe', fill=False, r=0.5)
box(ax, x0, 14, 4500*u, 9, 'resultat', label='4 500', r=0.5)
brace(ax, x0, x0 + 6000*u, 14, 'sujet', label='2bc = 6 000', down=True)
arrow(ax, (x0 + 1600*u + 4500*u/2, 40), (x0 + 4500*u/2, 24), 'varie')
text(ax, 44, 3, 'cos A = 4 500 / 6 000 = 0,75', 'resultat', 'm', weight='bold')
save(fig, '37-082')
