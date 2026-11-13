import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, 'couples de produit 1', 'sujet', 's')
f = numberline(ax, 10, 78, 20, -3, 3, arrow_right=False)
for v, a in [(-2, r'$-1$ et $-1$'), (2, r'$1$ et $1$')]:
    box(ax, f(v) - 13, 44, 26, 10, 'sujet', label=a, size='s')
    arrow(ax, (f(v), 44), (f(v), 24), 'sujet')
    disc(ax, f(v), 20, 1.6, 'sujet')
disc(ax, f(0), 20, 2.2, 'resultat', fill=False, lw=1.2)
text(ax, f(0), 36, 'somme voulue : 0', 'resultat', 's')
arrow(ax, (f(0), 33), (f(0), 24), 'resultat')
text(ax, f(0), 6, 'aucun couple n’y arrive', 'limite', 's')
save(fig, '18-096')
