import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
box(ax, 3, 87, 82, 9, 'sujet', label=r'$3+4i$ : chercher $x+iy$ de carré $3+4i$')
for cx in (22, 65):
    arrow(ax, (cx, 87), (cx, 80.5), 'fixe')
box(ax, 3, 71, 39, 9, 'sujet', label=r'$x^2-y^2=3$')
box(ax, 46, 71, 39, 9, 'sujet', label=r'$2xy=4$')
for cx in (22, 65):
    arrow(ax, (cx, 71), (cx, 64.5), 'fixe')
box(ax, 3, 53, 82, 11, 'varie', label='étape décisive, propriété (i) :\n' + r'$\sqrt{3^2+4^2}=\sqrt{25}=5$')
for cx in (22, 65):
    arrow(ax, (cx, 53), (cx, 46.5), 'fixe')
box(ax, 3, 37, 39, 9, 'fixe', label=r'$x^2+y^2=5$')
box(ax, 46, 37, 39, 9, 'fixe', label=r'$x^2-y^2=3$')
arrow(ax, (22, 37), (40, 30.5), 'fixe')
arrow(ax, (65, 37), (48, 30.5), 'fixe')
box(ax, 3, 21, 82, 9, 'fixe', label=r'on additionne : $2x^2=8$, donc $x^2=4$')
arrow(ax, (44, 21), (44, 14.5), 'fixe')
box(ax, 3, 3, 82, 11, 'resultat', label=r'$x=2$ et $y=1$ : $2xy=4=b$')
save(fig, '69-063')
