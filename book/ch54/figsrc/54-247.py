import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, r'$uf+vg$ évalué en 1, avec $f(1)=3$, $g(1)=0$', 'sujet', 's')
f = numberline(ax, 6, 74, 44, -6, 6, step=1, every=3, arrow_right=True, size='s')
for v in range(-6, 7):
    if v % 3 == 0:
        disc(ax, f(v), 44, 1.8, 'resultat')
disc(ax, f(1), 44, 1.8, 'limite')
text(ax, f(0), 54, 'multiples de 3 : atteints', 'resultat', 's')
arrow(ax, (f(3), 52), (f(3), 47.5), 'resultat')
text(ax, f(1), 28, '1 : jamais atteint', 'limite', 's')
arrow(ax, (f(1), 31), (f(1), 38), 'limite')
box(ax, 4, 3, 80, 13, 'autre', label=r'$\mathbb{Z}[x]$ n’est pas principal, $\mathbb{Z}$ l’est')
save(fig, '54-247')
