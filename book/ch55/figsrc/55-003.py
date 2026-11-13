import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 4, 62, 34, 14, 'sujet', label='Sophie\n' + r'$x^2-1$', size='s')
box(ax, 50, 62, 34, 14, 'autre', label='Théo\n' + r'$(x-1)(x+1)$', size='s')
rows = [(46, r'$3^2-1=8$', r'$(3-1)(3+1)=8$'), (28, r'$5^2-1=24$', r'$(5-1)(5+1)=24$')]
for y, a, b in rows:
    box(ax, 4, y - 6, 34, 12, 'sujet', label=a, size='s')
    box(ax, 50, y - 6, 34, 12, 'autre', label=b, size='s')
    text(ax, 44, y, '=', 'resultat', 'l')
box(ax, 4, 4, 34, 12, 'fixe', label='mêmes valeurs', size='s')
box(ax, 50, 4, 34, 12, 'resultat', label='mêmes coefficients', size='s')
arrow(ax, (38, 10), (50, 10), 'resultat')
text(ax, 44, 15, r'sur $\mathbb{R}$', 'resultat', 's')
save(fig, '55-003')
