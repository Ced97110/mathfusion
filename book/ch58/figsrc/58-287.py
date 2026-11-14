import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
ox, oy, u = 34, 12, 12.0
P = lambda x, y: (ox + x * u, oy + y * u)
for k in range(-1, 3):
    for l in range(0, 3):
        ax.plot([P(k, l)[0]], [P(k, l)[1]], 'o', ms=1.4, color=COL['fixe'], zorder=1)
arrow(ax, P(0, 0), P(1, 0), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(0, 1), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(-1, 2), 'varie', lw=1.5)
line(ax, [P(0, 0), P(-1, 0), P(-1, 2)], 'fixe', lw=0.7, dash=True)
text(ax, P(1, 0)[0] + 1, P(1, 0)[1] - 3, r'$u$ = (1, 0)', 'sujet', 's', ha='left')
text(ax, P(0, 1)[0] + 2, P(0, 1)[1] + 4, r'$v$ = (0, 1)', 'sujet', 's', ha='left')
text(ax, P(-1, 2)[0] - 2, P(-1, 2)[1] + 1, r'$w$ = (−1, 2)', 'varie', 's', ha='right')
text(ax, 70, 30, r'$w=-u+2v$', 'varie', 's')
text(ax, 70, 25.5, 'liée : on retire $w$', 'varie', 's')
text(ax, 70, 12, r'$(u,\ v)$ : une base', 'resultat', 's')
save(fig, '58-287')
