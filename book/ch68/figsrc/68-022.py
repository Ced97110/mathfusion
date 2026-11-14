import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 36, 53, 'reste de la division par 2', 'encre', 'm')
for y, n in [(40, '6'), (26, '100'), (12, '7')]:
    disc(ax, 14, y, 6, 'fixe', label=n, size='m')
line(ax, [(54, 8), (84, 8), (84, 46), (54, 46), (54, 8)], 'sujet', dash=True)
box(ax, 62, 32, 14, 9, 'sujet', label='0', size='l')
box(ax, 62, 13, 14, 9, 'sujet', label='1', size='l')
arrow(ax, (20.3, 40), (61.5, 37), 'varie')
arrow(ax, (20.3, 26), (61.5, 34.5), 'varie')
arrow(ax, (20.3, 12), (61.5, 16), 'varie')
text(ax, 69, 3.5, r'$\mathbb{F}_2=\mathbb{Z}/2\mathbb{Z}=\{0,1\}$', 'sujet', 'm')
save(fig, '68-022')
