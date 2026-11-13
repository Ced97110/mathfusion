import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy = 16, 10
P = lambda g, m: (ox + g, oy + m)
arrow(ax, (ox, oy), (ox + 58, oy), 'fixe'); arrow(ax, (ox, oy), (ox, oy + 58), 'fixe')
text(ax, ox + 63, oy, 'g', 'fixe', 'l'); text(ax, ox, oy + 59, 'm', 'fixe', 'l')
line(ax, [P(2, 0), P(2, 50), P(0, 50)], 'sujet', dash=True); line(ax, [P(50, 0), P(50, 2), P(0, 2)], 'limite', dash=True)
for v, r in [(2, 'sujet'), (50, 'limite')]:
    text(ax, ox + v, oy - 4, str(v), r, 's'); text(ax, ox - 4, oy + v, str(v), r, 's')
disc(ax, *P(2, 50), 1.8, 'sujet'); disc(ax, *P(50, 2), 1.8, 'limite')
text(ax, P(2, 50)[0] + 4, P(2, 50)[1] + 3, '(2, 50)', 'sujet', 'm', ha='left', weight='bold')
text(ax, P(50, 2)[0], P(50, 2)[1] + 6, '(50, 2)', 'limite', 'm', weight='bold')
text(ax, P(50, 2)[0], P(50, 2)[1] + 11, 'autre point', 'limite', 's')
save(fig, '09-116')
