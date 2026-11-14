import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 22, 72, 44, 10, 'sujet', label=r'$f$ irréductible')
text(ax, 44, 64, 'racine multiple possible\n' + r'seulement si $f^{\prime}=0$', 'encre', 's')
arrow(ax, (36, 59), (22, 49), 'fixe')
arrow(ax, (52, 59), (66, 49), 'fixe')
box(ax, 2, 38, 40, 10, 'resultat', label=r'PGCD $=1$')
y = 26
g = numberline(ax, 8, 36, y, -2, 2, 1, labels=False, arrow_right=False)
for v, lab in ((-1.414, r'$-\sqrt{2}$'), (1.414, r'$\sqrt{2}$')):
    disc(ax, g(v), y, 1.8, 'resultat'); text(ax, g(v), y - 5, lab, 'resultat', 's')
text(ax, 22, 8, 'racines distinctes', 'resultat', 's')
box(ax, 46, 38, 40, 10, 'varie', label=r'PGCD $=f$')
text(ax, 66, 29, r'$f$ divise $f^{\prime}$', 'varie', 'm')
text(ax, 66, 21, r'deg $f^{\prime}$ < deg $f$', 'varie', 's')
arrow(ax, (66, 18), (66, 13), 'varie')
box(ax, 46, 2, 40, 10, 'varie', label=r'seul cas : $f^{\prime}=0$', size='s')
save(fig, '62-104')
