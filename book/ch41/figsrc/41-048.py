import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-048 : vecteur de l'espace v = a i + b j + c k ; cas ⟨1 ; 2 ; 3⟩ = i + 2 j + 3 k (11 mm par unité, projection isométrique)
fig, ax = canvas(84)
u = 11
O = (50, 20)
P0 = iso(0, 0, 0, O, u); PA = iso(1, 0, 0, O, u); PB = iso(1, 2, 0, O, u); PV = iso(1, 2, 3, O, u)
# axes en gris fin
for q in [iso(2, 0, 0, O, u), iso(0, 3, 0, O, u), iso(0, 0, 4, O, u)]:
    arrow(ax, P0, q, 'fixe', lw=0.5)
arrow(ax, P0, PA, 'fixe', lw=2.0)
arrow(ax, PA, PB, 'fixe', lw=2.0)
arrow(ax, PB, PV, 'fixe', lw=2.0)
line(ax, [P0, PB], 'fixe', lw=0.6, dash=True)
arrow(ax, P0, PV, 'varie', lw=1.6)
text(ax, PA[0] + 2.5, PA[1] - 2.5, '1 $i$', 'fixe', 's', ha='left')
text(ax, (PA[0] + PB[0]) / 2 + 2, (PA[1] + PB[1]) / 2 + 3.5, '2 $j$', 'fixe', 's', ha='left')
text(ax, PB[0] - 2.5, (PB[1] + PV[1]) / 2, '3 $k$', 'fixe', 's', ha='right')
text(ax, PV[0] + 2.5, PV[1] + 1, '$v$', 'varie', 'l', ha='left', weight='bold')
for (q, s_, dx, dy) in [((2, 0, 0), 'axe $i$', 2.5, -1.5), ((0, 3, 0), 'axe $j$', -2.5, 1.5), ((0, 0, 4), 'axe $k$', 2.5, 0)]:
    T = iso(*q, O, u)
    text(ax, T[0] + dx, T[1] + dy, s_, 'encre', 's', ha='left' if dx > 0 else 'right', weight='bold')
text(ax, 44, 11,'$v = i + 2j + 3k$', 'encre', 'm')
text(ax, 44, 4, r'$= \langle$1 ; 2 ; 3$\rangle$', 'encre', 'm')
save(fig, '41-048')
