import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(48)
u = 12
def arc(cx, cy, r, a0, a1, role):
    n = 20
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts[:-1], role, lw=1.0)
    arrow(ax, pts[-2], pts[-1], role, lw=1.0)
# avant
cx, cy = 12, 14
text(ax, 24, 42, 'avant', 'encre', 'm', weight='bold')
arrow(ax, (cx, cy), (cx + u, cy), 'sujet', lw=1.3); text(ax, cx + u / 2, cy - 3.5, '1', 'sujet', 'm')
arrow(ax, (cx, cy), (cx, cy + 1.414 * u), 'varie', lw=1.3); text(ax, cx - 4, cy + 0.707 * u, r'$\sqrt{2}$', 'varie', 'm')
arc(cx, cy, 7, 5, 85, 'resultat')
text(ax, 25, 34, 'on tourne à gauche', 'resultat', 's', ha='center')
# apres
cx2 = 56
text(ax, 68, 42, r'après $\times\sqrt{2}$', 'encre', 'm', weight='bold')
arrow(ax, (cx2, cy), (cx2, cy + 1.414 * u), 'varie', lw=1.3); text(ax, cx2 - 4, cy + 0.707 * u, r'$\sqrt{2}$', 'varie', 'm')
arrow(ax, (cx2, cy), (cx2 + 2 * u, cy), 'sujet', lw=1.3); text(ax, cx2 + u, cy - 3.5, '2', 'sujet', 'm')
arc(cx2, cy, 7, 85, 5, 'limite')
text(ax, 70, 34, 'on tourne à droite', 'limite', 's')
line(ax, [(44, 8), (44, 40)], 'fixe', dash=True)
box(ax, 22, 2, 44, 7, 'autre', label=r'$\det=-2$ : sens inversé', size='m')
save(fig, '77-082')
