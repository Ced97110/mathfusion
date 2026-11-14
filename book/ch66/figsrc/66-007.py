import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X, Wd, H = 4, 80, 10
box(ax, X, 54, Wd, H, 'sujet', label=r'si $\sqrt{\pi}$ se construit', size='m')
box(ax, X, 36, Wd, H, 'sujet', label=r"$\sqrt{\pi}$ est racine d'un polynôme", size='m')
box(ax, X, 18, Wd, H, 'limite', label=r"donc $\pi$ racine d'un polynôme : faux", size='m')
box(ax, X, 2, Wd, H, 'resultat', label=r"à montrer : $\pi$ racine d'aucun polynôme", size='m')
for y in (54, 36):
    arrow(ax, (44, y), (44, y - 7.5), 'varie')
arrow(ax, (44, 18), (44, 12.5), 'resultat')
save(fig, '66-007')
