import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
o, u = (44, 30), 11.0
I = lambda x, y, z: iso(x, y, z, o, u)
# sol : plan de v et w ; u = <2, 3, 0> est dans ce plan
poly(ax, [I(0, 0, 0), I(3.2, 0, 0), I(3.2, 4.2, 0), I(0, 4.2, 0)], 'fixe')
arrow(ax, I(0, 0, 0), I(1, 0, 0), 'varie', lw=1.6)
arrow(ax, I(0, 0, 0), I(0, 1, 0), 'autre', lw=1.6)
arrow(ax, I(0, 0, 0), I(2, 3, 0), 'sujet', lw=1.6)
arrow(ax, I(0, 0, 0), I(0, 0, 4), 'resultat', lw=1.4)
text(ax, I(1, 0, 0)[0] + 3.5, I(1, 0, 0)[1] - 1, r'$v$', 'varie', 's')
text(ax, I(0, 1, 0)[0] - 3.5, I(0, 1, 0)[1] - 1, r'$w$', 'autre', 's')
text(ax, I(2, 3, 0)[0] - 4, I(2, 3, 0)[1] + 1.5, r'$u$', 'sujet', 's')
text(ax, I(0, 0, 4)[0] + 3, I(0, 0, 4)[1] + 1, r'$v\times w=\langle 0,\,0,\,1\rangle$', 'resultat', 's', ha='left')
text(ax, 4, 14, 'plan de $v$ et $w$ (gris)', 'fixe', 's', ha='left')
box(ax, 34, 3, 52, 20, 'resultat')
text(ax, 60, 17, r'$u\cdot(v\times w)=0$ ⇒', 'resultat', 's', weight='bold')
text(ax, 60, 9, r'$u$ est dans le plan de $v$, $w$', 'resultat', 's')
save(fig, '41-156')
