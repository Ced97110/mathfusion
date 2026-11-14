import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
O = (42, 33)
pts = {'(1, 0)': (1, 0), '(0, 1)': (0, 1), '(2, 0)': (-1, 0), '(0, 2)': (0, -1)}
for lab, (dx, dy) in pts.items():
    p = (O[0] + 16 * dx, O[1] + 16 * dy)
    arrow(ax, O, (p[0] - 2.6 * dx, p[1] - 2.6 * dy), 'sujet', lw=1.2)
    disc(ax, p[0], p[1], 1.6, 'sujet')
    text(ax, O[0] + 26 * dx, O[1] + 21.5 * dy, lab, 'sujet', 's')
disc(ax, *O, 1.5, 'fixe')
text(ax, 42, 61, r'$Q(y)=y_1^2+y_2^2=1$', 'encre', 'm')
text(ax, 42, 3, '4 flèches y', 'resultat', 'm')
save(fig, '75-131')
