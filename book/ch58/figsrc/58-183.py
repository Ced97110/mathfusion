import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# deux bases du plan, chacune de 2 vecteurs : un seul nombre
def plan(x0, title, v1, v2, u):
    box(ax, x0, 28, 38, 40, 'fixe', fill=False, dash=True)
    text(ax, x0 + 19, 63, title, 'sujet', 'm', weight='bold')
    ox, oy = x0 + 8, 36
    for v in (v1, v2):
        arrow(ax, (ox, oy), (ox + v[0] * u, oy + v[1] * u), 'sujet', lw=1.5)
    t1 = f'({v1[0]}, {v1[1]})'; t2 = f'({v2[0]}, {v2[1]})'
    text(ax, ox + v1[0] * u + 1.2, oy + v1[1] * u - 0.5, t1, 'sujet', 's', ha='left')
    text(ax, ox + v2[0] * u + 1.2, oy + v2[1] * u + 2.2, t2, 'sujet', 's', ha='left')
    text(ax, x0 + 19, 22, '2 vecteurs', 'sujet', 's')
    arrow(ax, (x0 + 19, 19.5), (x0 + 19, 15), 'resultat', lw=1.0)
plan(3, 'base 1', (1, 0), (0, 1), 12)
plan(47, 'base 2', (3, 1), (1, 2), 6)
box(ax, 14, 3, 60, 11, 'resultat', label='un seul nombre pour le plan : 2', size='m', weight='bold')
save(fig, '58-183')
