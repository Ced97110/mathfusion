import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'$f=(y-1)^2$, $g=(y-1)(y+1)$', 'encre', 'm')
text(ax, 71, 62, r'racines de $g$', 'autre', 's')
text(ax, 43, 56, r'$s_1=1$', 'autre', 'm')
text(ax, 71, 56, r'$s_2=-1$', 'autre', 'm')
text(ax, 13, 56, 'racines de $f$\n(1 double)', 'sujet', 's')
for i, y in enumerate([38, 24]):
    text(ax, 13, y + 5, rf'$r_{i + 1}=1$', 'sujet', 'm')
    box(ax, 30, y, 26, 10, 'resultat', label=r'$1-1=0$', size='s')
    box(ax, 58, y, 26, 10, 'fixe', label=r'$1+1=2$', size='s')
arrow(ax, (43, 22), (43, 17), 'resultat')
box(ax, 8, 4, 76, 12, 'resultat', label=r'deux cases à $0$ : produit $=0$, donc $\mathrm{Res}=0$', size='s')
save(fig, '70-117')
