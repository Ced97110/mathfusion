import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, s = 14, 12, 11
for k in range(0, 5):
    line(ax, [(ox + k * s, oy), (ox + k * s, oy + 4 * s)], 'fixe', lw=0.3)
    line(ax, [(ox, oy + k * s), (ox + 4 * s, oy + k * s)], 'fixe', lw=0.3)
arrow(ax, (ox - 4, oy), (ox + 4 * s + 6, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 4), (ox, oy + 4 * s + 6), 'fixe', lw=0.8)
a, b = 2, 3
arrow(ax, (ox, oy), (ox + a * s - 1.2, oy), 'varie', lw=1.6)
arrow(ax, (ox + a * s, oy), (ox + a * s, oy + b * s - 1.5), 'autre', lw=1.6)
line(ax, [(ox, oy + b * s), (ox + a * s, oy + b * s)], 'fixe', lw=0.7, dash=True)
disc(ax, ox + a * s, oy + b * s, 1.6, 'sujet')
text(ax, ox + a * s / 2, oy - 3.2, '$a$ = 2 vers la droite', 'varie', 's')
text(ax, ox + a * s + 3, oy + b * s / 2, '$b$ = 3 vers\nle haut', 'autre', 's', ha='left')
text(ax, ox + a * s + 3, oy + b * s + 3.5, '$2+3i$ = point (2 ; 3)', 'sujet', 'm', ha='left')
text(ax, 44, 66, '$a+bi$  ↔  point ($a$ ; $b$)', 'encre', 'l')
save(fig, '62-013')
