import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# base 1 : e1, e2, e3 (unité 10 mm) ; base 2 : trois vecteurs (unité 5 mm)
O1 = (22, 24); U1 = 10.0
for v, lab, dx, dy, ha in [((1, 0, 0), r'$e_1$', 1.5, -2, 'left'), ((0, 1, 0), r'$e_2$', -1.5, -2, 'right'), ((0, 0, 1), r'$e_3$', 0, 3, 'center')]:
    p = iso(*v, O1, U1)
    arrow(ax, O1, p, 'sujet', lw=1.3)
    text(ax, p[0] + dx, p[1] + dy, lab, 'sujet', 's', ha=ha)
O2 = (64, 24); U2 = 5.0
for v, lab, dx, dy, ha in [((3, 2, 1), '(3, 2, 1)', 2, 1, 'left'), ((3, 2, 0), '(3, 2, 0)', 2, -1, 'left'), ((1, 1, 1), '(1, 1, 1)', -2, 1, 'right')]:
    p = iso(*v, O2, U2)
    arrow(ax, O2, p, 'autre', lw=1.3)
    text(ax, p[0] + dx, p[1] + dy, lab, 'autre', 's', ha=ha)
text(ax, 22, 8, 'une base : 3 vecteurs', 'sujet', 's')
text(ax, 64, 8, 'une autre base : 3 vecteurs', 'autre', 's')
text(ax, 44, 58, r'deux bases de $\mathbb{R}^3$', 'fixe', 's')
save(fig, '58-169')
