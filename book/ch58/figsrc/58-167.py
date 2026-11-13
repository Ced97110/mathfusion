import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# plan engendré par u = (1, 2, 1) et v = (0, 1, -1), en projection isométrique
O = (30, 40); U = 9.0
a = iso(1, 2, 1, O, U); b = iso(0, 1, -1, O, U)
ab = (a[0] + b[0] - O[0], a[1] + b[1] - O[1])
poly(ax, [O, a, ab, b], 'fixe')
arrow(ax, O, a, 'sujet', lw=1.3)
arrow(ax, O, b, 'varie', lw=1.3)
text(ax, a[0] + 1, a[1] + 3.5, r'$u=(1,2,1)$', 'sujet', 's', ha='left')
text(ax, b[0] + 1, b[1] - 3.5, r'$v=(0,1,-1)$', 'varie', 's', ha='left')
text(ax, 22, 76, 'le plan qu’ils engendrent', 'fixe', 's')
# deux vérifications
box(ax, 46, 56, 38, 22, 'resultat')
text(ax, 65, 73, 'base de ce plan', 'resultat', 's', weight='bold')
text(ax, 65, 66, 'indépendants  ✓', 'resultat', 's')
text(ax, 65, 60, 'engendrent le plan  ✓', 'resultat', 's')
box(ax, 46, 22, 38, 22, 'limite')
text(ax, 65, 39, 'pas base de l’espace', 'limite', 's', weight='bold')
text(ax, 65, 32, 'indépendants  ✓', 'resultat', 's')
text(ax, 65, 26, 'engendrent l’espace  ✗', 'limite', 's')
text(ax, 44, 8, 'une base se juge pour un espace donné', 'fixe', 's')
save(fig, '58-167')
