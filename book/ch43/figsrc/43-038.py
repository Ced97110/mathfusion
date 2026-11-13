import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, u = 32, 31, 5.5
disc(ax, cx, cy, 5 * u, 'fixe', fill=False)
line(ax, [(cx - 29, cy), (cx + 29, cy)], 'fixe', lw=0.6); line(ax, [(cx, cy - 29), (cx, cy + 29)], 'fixe', lw=0.6)
P1, P2 = (cx + 3 * u, cy + 4 * u), (cx + 5 * u, cy)
line(ax, [(cx, cy), P1], 'varie', lw=1.1); line(ax, [(cx, cy), P2], 'varie', lw=1.1)
disc(ax, *P1, 1.5, 'sujet'); disc(ax, *P2, 1.5, 'autre'); disc(ax, cx, cy, 1.0, 'encre')
text(ax, cx - 3, cy - 3, r'$O$', 'encre', 's')
text(ax, 37, 45, '5', 'varie', 's'); text(ax, 45, cy + 3, '5', 'varie', 's')
text(ax, 62, 55, '(3, 4)', 'sujet', 's', ha='left'); text(ax, 62, 50, '9 + 16 = 25', 'sujet', 's', ha='left')
text(ax, 65, 26, '(5, 0)', 'autre', 's', ha='left'); text(ax, 65, 21, '25 + 0 = 25', 'autre', 's', ha='left')
save(fig, '43-038')
