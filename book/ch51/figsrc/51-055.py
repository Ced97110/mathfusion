import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$\lambda_3$ : $x\mapsto 3x$ sur le cadran à 7 h', 'sujet', 'm')
text(ax, 16, 53, r'$x$ varie', 'varie', 'm'); text(ax, 72, 53, r'$3x$', 'resultat', 'm')
text(ax, 44, 53, r'$a=3$ fixé', 'fixe', 'm')
for k, (a, b) in enumerate([(1, 3), (2, 6), (4, 5)]):
    y = 38 - k * 14
    box(ax, 8, y - 5, 16, 10, 'varie', label=str(a), size='l')
    box(ax, 64, y - 5, 16, 10, 'resultat', label=str(b), size='l')
    arrow(ax, (25, y), (63, y), 'fixe')
text(ax, 44, 4, '4 × 3 = 12, soit 5', 'fixe', 's')
save(fig, '51-055')
