import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 44, 80, r'$n=2$, $q=3$ : diviseurs 1 et 2', 'encre', 's')
rows = [(r'$d=1$', r'$\mu(2)\times3^1$', r'$=-3$', 'varie'),
        (r'$d=2$', r'$\mu(1)\times3^2$', r'$=9$', 'sujet')]
for i, (a, b, c, r) in enumerate(rows):
    y = 62 - i * 17
    box(ax, 2, y - 6, 18, 12, 'fixe', label=a, size='s')
    box(ax, 24, y - 6, 38, 12, r, label=b, size='s')
    box(ax, 66, y - 6, 20, 12, r, label=c, size='s')
    arrow(ax, (20.8, y), (23.2, y), 'fixe'); arrow(ax, (62.8, y), (65.2, y), 'fixe')
box(ax, 14, 24, 60, 11, 'autre', label=r'somme : $9-3=6$', size='s')
arrow(ax, (44, 25), (44, 18), 'fixe')
box(ax, 14, 6, 60, 11, 'resultat', label=r'$\div\,n=2$ : $N(2,3)=3$', size='s')
save(fig, '67-119')
