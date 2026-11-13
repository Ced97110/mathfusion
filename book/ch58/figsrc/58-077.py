import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 10, 74, 24, -2, 2, 1, arrow_right=False)
for v, lab in [(-2, '−1 × 2'), (0, '0 × 2'), (2, '1 × 2')]:
    disc(ax, f(v), 24, 1.4, 'limite')
    text(ax, f(v), 31, lab, 'limite', 's')
disc(ax, f(1), 24, 2.4, 'resultat', fill=False, lw=1.2)
text(ax, f(1), 39, 'cible : 1', 'resultat', 'm')
arrow(ax, (f(1), 37), (f(1), 28), 'resultat', lw=0.9)
text(ax, 44, 8, 'aucun entier × 2 ne donne 1', 'limite', 's')
save(fig, '58-077')
