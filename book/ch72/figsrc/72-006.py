import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)

fig, ax = canvas(80)
u = 9
def panel(ox, oy):
    axes(ax, ox, oy, u, -1.5, 2.1, -0.8, 2.3)
    return lambda x, y: (ox + x * u, oy + y * u)
P = panel(22, 44)
line(ax, [P(-1.4, 0), P(2.1, 0)], 'varie', lw=1.3)
for x in (-1, 1, 2):
    disc(ax, *P(x, 0), 1.2, 'resultat')
text(ax, 22, 74, 'un pli', 'varie', 'm', weight='bold')
text(ax, 22, 26, 'points fixes : la droite', 'resultat', 's')
Q = panel(66, 44)
disc(ax, *Q(0, 0), 1.2, 'resultat')
disc(ax, *Q(1, 0), 1.4, 'sujet'); disc(ax, *Q(0, 1), 1.4, 'sujet', fill=False)
arrow(ax, Q(1, 0.3), Q(0.3, 1), 'varie', lw=1.0, curve=0.4)
text(ax, Q(1, 0)[0] + 1, Q(1, 0)[1] - 4, '(1, 0)', 'sujet', 's')
text(ax, Q(0, 1)[0] - 1, Q(0, 1)[1] + 3.5, '(0, 1)', 'sujet', 's', ha='right')
text(ax, 66, 74, 'quart de tour', 'varie', 'm', weight='bold')
text(ax, 66, 26, 'point fixe : la croix', 'resultat', 's')
box(ax, 4, 2, 38, 18, 'limite', label=None)
text(ax, 23, 14, r'$n=2$ : 1 pli', 'limite', 'm'); text(ax, 23, 7, 'ne suffit pas', 'limite', 's')
box(ax, 46, 2, 38, 18, 'resultat', label=None)
text(ax, 65, 14, r'$n$ dimensions', 'resultat', 'm'); text(ax, 65, 7, r'$n$ plis au plus', 'resultat', 'm')
save(fig, '72-006')
