import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
box(ax, 10, 72, 68, 11, 'sujet', label=r'départ : $|G|=p^k$', size='m')
box(ax, 10, 55, 68, 11, 'varie', label=r"Lagrange : l'ordre divise $|G|$", size='m', lw=1.8)
box(ax, 10, 38, 68, 11, 'resultat', label=r"arrivée : ordre = $p^j$", size='m')
arrow(ax, (44, 72), (44, 66.5), 'encre'); arrow(ax, (44, 55), (44, 49.5), 'encre')
line(ax, [(2, 33), (86, 33)], 'fixe', dash=True)
text(ax, 3, 28, r'$\mathbb{Z}/8\mathbb{Z}$, élément 2', 'encre', 's', ha='left')
for i in range(8):
    even = i % 2 == 0
    disc(ax, 12 + 9 * i, 17, 3.6, 'varie' if even else 'fixe', label=str(i) if even else None, size='s')
brace(ax, 8, 80, 11, 'varie', label='ordre 4 divise 8 éléments')
save(fig, '50-030')
