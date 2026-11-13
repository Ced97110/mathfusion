import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'sur $\mathbb{Z}$ : $u=\pm1$ seulement', 'encre', 'l')
# ligne A : x3, impossible à défaire
box(ax, 5, 42, 14, 9, 'sujet', label='$L$')
box(ax, 54, 42, 18, 9, 'fixe', label='$3L$')
arrow(ax, (20, 46.5), (53, 46.5), 'varie', lw=1.2); text(ax, 36, 50.5, r'$\times3$', 'varie', 's')
arrow(ax, (63, 41), (12, 41), 'limite', lw=1.2, curve=-0.25)
text(ax, 38, 30, r'retour $\times\frac{1}{3}\notin\mathbb{Z}$', 'limite', 's')
# ligne B : x(-1), se défait
box(ax, 5, 14, 14, 9, 'sujet', label='$L$')
box(ax, 54, 14, 18, 9, 'resultat', label='$-L$')
arrow(ax, (20, 18.5), (53, 18.5), 'varie', lw=1.2); text(ax, 36, 22.5, r'$\times(-1)$', 'varie', 's')
arrow(ax, (63, 13), (12, 13), 'resultat', lw=1.2, curve=-0.25)
text(ax, 38, 5, r'retour $\times(-1)$ : entier', 'resultat', 's')
save(fig, '59-056')
