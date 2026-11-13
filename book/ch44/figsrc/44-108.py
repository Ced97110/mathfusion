import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'$H$ = nombres pairs dans $\mathbb{Z}$', 'sujet', 'm')
L = [r'$1 \in H$', r'$H$ stable', r'inverses dans $H$']
R = ['0 est pair', 'pair + pair = pair', 'opposé de pair = pair']
for i in range(3):
    y = 50 - i * 17
    box(ax, 2, y, 32, 12, 'sujet', label=L[i], size='s')
    arrow(ax, (34, y + 6), (42, y + 6), 'varie')
    box(ax, 42, y, 44, 12, 'resultat')
    text(ax, 64, y + 6, '✓ ' + R[i], 'resultat', 's')
text(ax, 44, 7, 'trois conditions suffisent', 'fixe', 'm')
save(fig, '44-108')
