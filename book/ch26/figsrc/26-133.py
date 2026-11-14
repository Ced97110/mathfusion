import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
ox, oy, u = 10, 10, 15
arrow(ax, (ox - 3, oy), (ox + 4.4 * u, oy), 'fixe', lw=0.9); arrow(ax, (ox, oy - 3), (ox, oy + 4.4 * u), 'fixe', lw=0.9)
line(ax, [(ox, oy), (ox + 4 * u, oy + 4 * u)], 'sujet', lw=1.6)
text(ax, ox + 2.9 * u, oy + 3.5 * u, 'y = x', 'sujet', 'm', ha='right', weight='bold')
for k in (1, 2, 3):
    disc(ax, ox + k * u, oy + k * u, 1.1, 'sujet')
for k in (1, 2):
    arrow(ax, (ox + k * u, oy + k * u), (ox + (k + 1) * u - 1.5, oy + k * u), 'varie')
    arrow(ax, (ox + (k + 1) * u, oy + k * u + 1.5), (ox + (k + 1) * u, oy + (k + 1) * u - 1.5), 'varie')
text(ax, ox + 2.5 * u, oy + 2 * u - 3, 'avance 1', 'varie', 's')
text(ax, ox + 3 * u + 1.5, oy + 2.5 * u - 3, 'monte 1', 'varie', 's', ha='left')
import math
pts = [(ox + 22 * math.cos(t), oy + 22 * math.sin(t)) for t in [math.pi / 4 * i / 20 for i in range(21)]]
line(ax, pts, 'resultat', lw=1.2)
text(ax, ox + 27, oy + 9, 'θ = 45°', 'resultat', 'm', ha='left')
text(ax, ox + 2 * u, oy + 3.7 * u + 4, 'pente = 1', 'sujet', 'm', ha='right') if False else None
box(ax, 58, 22, 28, 16, 'resultat'); text(ax, 72, 34, 'pente 1', 'resultat', 's'); text(ax, 72, 27, 'tan 45° = 1', 'resultat', 's')
save(fig, '26-133')
