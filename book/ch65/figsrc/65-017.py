import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, U = 12, 36, 10.0
arrow(ax, (3, oy), (ox + 6.4 * U, oy), 'fixe', lw=0.8)
arrow(ax, (ox, 6), (ox, 68), 'fixe', lw=0.8)
text(ax, 78, oy - 3.5, 'réels', 'fixe', 's')
text(ax, ox + 11, 67, 'imaginaires', 'fixe', 's')
for v in (3, 5):
    line(ax, [(ox + U * v, oy - 1), (ox + U * v, oy + 1)], 'fixe')
text(ax, ox + 3 * U, oy - 4, '3', 'fixe', 's')
# 3 + 2i et 3 - 2i
a, b = (ox + 3 * U, oy + 2 * U), (ox + 3 * U, oy - 2 * U)
disc(ax, *a, 1.5, 'sujet'); disc(ax, *b, 1.5, 'sujet')
text(ax, a[0] + 11, a[1], '$3+2i$', 'sujet', 'm')
text(ax, b[0] + 11, b[1], '$3-2i$', 'sujet', 'm')
arrow(ax, (a[0], a[1] - 2.5), (b[0], b[1] + 2.5), 'varie', both=True)
text(ax, a[0] - 7.5, oy + 1.8, 'échange', 'varie', 's')
# 5 reste en place
disc(ax, ox + 5 * U, oy, 1.5, 'fixe')
text(ax, ox + 5 * U, oy + 5, '5 reste', 'fixe', 's')
text(ax, 44, 4, r'$a+bi\mapsto a-bi$  comme  $(r_2\ r_3)$', 'varie', 's')
save(fig, '65-017')
