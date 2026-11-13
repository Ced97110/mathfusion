import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xs = [10 + 11 * k for k in range(7)]
for k, x in enumerate(xs):
    text(ax, x, 28, 'b' if k % 2 == 0 else 'p', 'sujet' if k % 2 == 0 else 'autre', 'xl', weight='bold')
arrow(ax, (xs[0], 35), (xs[2], 35), 'resultat', curve=-0.5, lw=1.4)
text(ax, xs[1], 46, r'glisse de 2 lettres : dans $T$', 'resultat', 's')
arrow(ax, (xs[2], 21), (xs[3], 21), 'limite', curve=0.5, lw=1.4)
text(ax, 58, 8, r'retourne + glisse de 1 : hors de $T$', 'limite', 's')
text(ax, 44, 53, r'$T$ : les glissements purs de $G$', 'sujet', 's')
save(fig, '74-103')
