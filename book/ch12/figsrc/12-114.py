import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 24, 46, 40, 13, 'sujet', label=r'$x+4>6$', size='xl')
cases = [(1, r'$x=1$', r'$5>6$', 'faux', 'limite'), (2, r'$x=2$', r'$6>6$', 'faux', 'limite'),
         (3, r'$x=3$', r'$7>6$', 'vrai', 'resultat')]
for i, (v, a, b, c, role) in enumerate(cases):
    x = 3 + i * 29.5
    box(ax, x, 10, 24, 25, role)
    text(ax, x + 12, 29, a, 'encre', 'm'); text(ax, x + 12, 22.5, b, role, 'l'); text(ax, x + 12, 15, c, role, 'm', weight='bold')
    arrow(ax, (44, 46), (x + 12, 36), 'varie')
text(ax, 44, 4, 'vraie pour certaines valeurs', 'encre', 's')
save(fig, '12-114')
