import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 22, 56, 44, 11, 'sujet', label=r'$x \mapsto 3x$ sur $\mathbb{Z}$', size='m')
cards = [(2, '4 et 5', '3 × 9 = 27', '12 + 15 = 27'),
         (46, '7 et −2', '3 × 5 = 15', '21 + (−6) = 15')]
for (x, a, b, c) in cards:
    text(ax, x + 20, 48, a, 'sujet', 'm')
    box(ax, x, 33, 40, 10, 'varie', label=b, size='s')
    box(ax, x, 18, 40, 10, 'varie', label=c, size='s')
    text(ax, x + 20, 30.5, '=', 'resultat', 'm')
text(ax, 44, 8, r'$3(x+y)=3x+3y$ : même résultat', 'resultat', 's')
save(fig, '57-039')
