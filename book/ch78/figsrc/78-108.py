import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = numberline(ax, 8, 74, 24, 1, 8, arrow_right=True)
for d in range(1, 9):
    ok = d in (1, 2, 4, 8)
    disc(ax, f(d), 34, 2.6, 'resultat' if ok else 'limite')
    line(ax, [(f(d), 31.4), (f(d), 25.5)], 'resultat' if ok else 'limite', lw=0.6, dash=True)
text(ax, 4, 14, 'dimension', 'fixe', 's', ha='left')
box(ax, 4, 46, 38, 10, 'resultat', label=r'$Q(xy)=Q(x)Q(y)$', size='s')
box(ax, 46, 46, 38, 10, 'limite', label='forme non conservée', size='s')
text(ax, 44, 4, 'dim. 3 : produit terme à terme', 'limite', 's')
save(fig, '78-108')
