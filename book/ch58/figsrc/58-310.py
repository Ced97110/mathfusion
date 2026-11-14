import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 13; ox, oy = 26, 24
p = lambda x, y: (ox + x * u, oy + y * u)
# les deux axes = couples envoyés sur 0
line(ax, [p(-1.6, 0), p(2.0, 0)], 'sujet', lw=2.0)
line(ax, [p(0, -1.0), p(0, 2.0)], 'sujet', lw=2.0)
# somme (1, 0) + (0, 1)
line(ax, [p(1, 0), p(1, 1), p(0, 1)], 'fixe', lw=0.8, dash=True)
for q, r in (((1, 0), 'sujet'), ((0, 1), 'sujet'), ((1, 1), 'limite')):
    disc(ax, p(*q)[0], p(*q)[1], 1.5, r)
text(ax, p(1, 0)[0] + 3, p(1, 0)[1] - 4, '(1, 0)', 'sujet', 's')
text(ax, p(0, 1)[0] - 9, p(0, 1)[1] + 1, '(0, 1)', 'sujet', 's')
text(ax, p(1, 1)[0] + 8, p(1, 1)[1] + 3, '(1, 1)', 'limite', 's')
text(ax, 44, 61, r'$\eta(x,\ y) = x \cdot y$', 'encre', 'm')
x0 = 58
text(ax, x0, 51, '(1, 0) ↦ 0', 'sujet', 's', ha='left')
text(ax, x0, 45, '(0, 1) ↦ 0', 'sujet', 's', ha='left')
text(ax, x0, 37, '(1, 1) ↦ 1, pas 0 + 0', 'limite', 's', ha='left')
box(ax, 46, 4, 40, 12, 'limite', label='les deux axes ne forment\npas un sous-espace', size='s')
save(fig, '58-310')
