import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
ux, uy = 12, 9
for ox, role, hd in [(8, 'sujet', 'pente 3'), (46, 'autre', r'pente $\frac{1}{2}$')]:
    P = lambda x, y: (ox + x * ux, 8 + y * uy)
    arrow(ax, (ox, 8), (ox + 2.6 * ux, 8), 'fixe', lw=0.8)
    text(ax, ox + 14, 43, hd, role, 'l')
    if role == 'sujet':
        line(ax, [P(0, 0), P(1.05, 3.15)], role, lw=1.5)
        arrow(ax, P(0, 0), P(1, 0), 'fixe', lw=1.0); arrow(ax, P(1, 0), P(1, 3), 'varie', lw=1.2)
        text(ax, P(0.5, 0)[0], 4, '1', 'fixe', 's'); text(ax, P(1, 1.5)[0] + 3, P(0, 1.5)[1], '3', 'varie', 'm', ha='left')
    else:
        line(ax, [P(0, 0), P(2.4, 1.2)], role, lw=1.5)
        for k in range(2):
            arrow(ax, P(k, k / 2), P(k + 1, k / 2), 'fixe', lw=1.0); arrow(ax, P(k + 1, k / 2), P(k + 1, k / 2 + 0.5), 'varie', lw=1.2)
        text(ax, P(0.5, 0)[0], 4, '1', 'fixe', 's'); text(ax, P(1, 0.25)[0] + 3, P(0, 0.25)[1], r'$\frac{1}{2}$', 'varie', 'm', ha='left')
        text(ax, ox + 14, 31, 'pas de 2 : monte 1', 'fixe', 's')
save(fig, '19-080')
