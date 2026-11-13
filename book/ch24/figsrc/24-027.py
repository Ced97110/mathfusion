import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
U = 6.0; OY = 12
def P(ox, x, y): return (ox + x * U, OY + y * U)
for ox in (7, 49):
    line(ax, [P(ox, 0, 0), P(ox, 6, 0)], 'fixe'); line(ax, [P(ox, 0, 0), P(ox, 0, 6)], 'fixe')
# left: parallel D1 (x+y=5), D3 (x+y=8)
line(ax, [P(7, 0, 5), P(7, 5, 0)], 'sujet', lw=1.2)
line(ax, [P(7, 2, 6), P(7, 6, 2)], 'autre', lw=1.2)
for x, a, b in ((2, 3, 6), (4, 1, 4)):
    line(ax, [P(7, x, a), P(7, x, b)], 'varie', lw=1.1)
    text(ax, P(7, x, 0)[0], OY - 3.5, str(x), 'fixe', 's')
    text(ax, P(7, x, (a + b) / 2)[0] + 3, P(7, x, (a + b) / 2)[1], '3', 'varie', 's')
text(ax, *P(7, 0.9, 5.4), r'$D_1$', 'sujet', 'm'); text(ax, *P(7, 5.0, 5.0), r'$D_3$', 'autre', 'm')
text(ax, 25, 54, 'aucune solution', 'encre', 's')
# right: coincident D1 and D4 (dashed)
pa, pb = P(49, 0, 5), P(49, 5, 0)
line(ax, [pa, pb], 'sujet', lw=1.4); line(ax, [pa, pb], 'autre', lw=1.4, dash=True)
text(ax, *P(49, 1.0, 5.4), r'$D_1$', 'sujet', 'm'); text(ax, *P(49, 4.4, 1.8), r'$D_4$', 'autre', 'm')
text(ax, 67, 54, 'une infinité', 'encre', 's')
save(fig, '24-027')
