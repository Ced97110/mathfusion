import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, u = 20, 24, 20
Q = lambda x, y: (ox + x * u, oy + y * u)
line(ax, [(ox - 12, oy - 12), (ox + 30, oy + 30)], 'fixe', lw=1.2, dash=True)
text(ax, ox + 25, oy + 33, r'pli de $S_w$', 'fixe', 's')
arrow(ax, Q(0, 0), Q(1, 0), 'sujet', lw=1.5)
arrow(ax, Q(0, 0), Q(0, 1), 'varie', lw=1.5)
import math
pts = [(ox + 1.15 * u * math.cos(math.radians(6 + k * 3)), oy + 1.15 * u * math.sin(math.radians(6 + k * 3))) for k in range(27)]
line(ax, pts[:-2], 'varie', lw=1.0)
arrow(ax, pts[-3], pts[-1], 'varie', lw=1.0)
arrow(ax, Q(0.08, 0.92), Q(0.92, 0.08), 'resultat', lw=1.3)
text(ax, Q(1, 0)[0] + 3, Q(1, 0)[1] - 3, r'$u$', 'sujet', 'm')
text(ax, Q(0, 1)[0] - 4, Q(0, 1)[1] + 1, r'$\eta u$', 'varie', 'm')
text(ax, 12, 56, r'$\eta$ envoie $u$ sur $\eta u$', 'varie', 's', ha='left')
text(ax, 52, 40, r"$S_w$ le ramène sur $u$", 'resultat', 's') if False else None
box(ax, 54, 38, 31, 11, 'resultat', label=r"$\eta' = S_w\,\eta$", size='s')
box(ax, 54, 24, 31, 11, 'resultat', label=r"$\eta'$ fixe $u$", size='s')
box(ax, 54, 10, 31, 11, 'sujet', label=r"garde $u^{\perp}$", size='s')
arrow(ax, (69.5, 37.5), (69.5, 35.5), 'fixe', lw=0.6); arrow(ax, (69.5, 23.5), (69.5, 21.5), 'fixe', lw=0.6)
text(ax, 69.5, 4, r'puis dimension $n-1$', 'sujet', 's')
text(ax, 52, 56, '', 'fixe', 's')
save(fig, '72-138')
