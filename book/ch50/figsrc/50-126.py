import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 4, 50, 80, 10, 'sujet', label=r'groupe abélien, $p$ premier divise $|G|$', size='s')
arrow(ax, (44, 50), (44, 43), 'resultat')
text(ax, 44, 39, r'il existe un élément d’ordre $p$', 'resultat', 's', weight='bold')
text(ax, 44, 30, r'exemple : $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$, $p=2$', 'sujet', 's')
for i, xx in enumerate([15, 34, 53, 72]):
    disc(ax, xx, 17, 5, 'fixe' if i == 0 else 'resultat', label='$e$' if i == 0 else None)
    text(ax, xx, 8, r'ordre $1$' if i == 0 else r'ordre $2$', 'fixe' if i == 0 else 'resultat', 's')
text(ax, 44, 2.5, r'ordre $2$ : $x\cdot x=e$', 'resultat', 's')
save(fig, '50-126')
