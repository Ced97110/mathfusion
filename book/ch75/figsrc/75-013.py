import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
u, oy = 14, 10
for ox in (6, 46):
    arrow(ax, (ox, oy), (ox + 2 * u + 6, oy), 'fixe', lw=0.7); arrow(ax, (ox, oy), (ox, oy + u + 8), 'fixe', lw=0.7)
arrow(ax, (6, oy), (6 + u, oy), 'sujet', lw=1.3); arrow(ax, (6, oy), (6, oy + u), 'sujet', lw=1.3)
text(ax, 13, oy - 4, r'$e$ = (1, 0)', 'sujet', 's'); text(ax, 6, oy + u + 4, r'$f$ = (0, 1)', 'sujet', 's', ha='left')
arrow(ax, (46, oy), (46 + 2 * u, oy + u), 'varie', lw=1.3); arrow(ax, (46, oy), (46 + u, oy + u), 'autre', lw=1.3)
text(ax, 46 + 2 * u + 2, oy + u + 4.5, r'$\eta e$ = (2, 1)', 'varie', 's'); text(ax, 46 + u - 2, oy + u + 4.5, r'$\eta f$ = (1, 1)', 'autre', 's', ha='right')
arrow(ax, (26, 20), (42, 20), 'varie', lw=1.3); text(ax, 34, 24.5, r'$\eta$', 'varie', 'l')
save(fig, '75-013')
