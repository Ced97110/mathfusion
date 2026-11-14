import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy, u = 22, 18, 30
line(ax, [(ox - 0.5 * u - 2, oy), (ox + 1.4 * u, oy)], 'fixe', lw=0.6)
line(ax, [(ox, oy - 2), (ox, oy + 1.75 * u)], 'fixe', lw=0.6)
xs = [-0.5 + i * 0.025 for i in range(0, 71)]
line(ax, [(ox + x * u, oy + x * x * u) for x in xs], 'sujet', lw=1.4)
line(ax, [(ox - 0.5 * u, oy - 0.5 * u), (ox + 1.25 * u, oy + 1.25 * u)], 'autre', lw=1.4)
text(ax, ox + 1.2 * u + 6, oy + 1.2 * u * 1.2 - 2, 'y = x²', 'sujet', 's')
text(ax, ox + 1.25 * u + 6, oy + 1.25 * u - 4, 'y = x', 'autre', 's')
disc(ax, ox, oy, 2.2, 'limite', fill=False, lw=1.2)
disc(ax, ox + u, oy + u, 2.2, 'resultat')
text(ax, ox + 6, oy - 7, 'x = 0 : perdue par ÷ x', 'limite', 's', ha='left')
text(ax, ox + u + 4, oy + u - 6, 'x = 1', 'resultat', 's', ha='left')
text(ax, 44, 74, 'x² = x : deux solutions', 'encre', 's')
save(fig, '32-126')
