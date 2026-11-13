import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(68)
ox, oy = 6, 20
P = lambda r, d: (ox + r * math.cos(math.radians(d)), oy + r * math.sin(math.radians(d)))
def arc(r, d0, d1, role):
    line(ax, [P(r, d) for d in np.linspace(d0, d1, 30)], role)
line(ax, [(ox, oy), (ox + 76, oy)], 'fixe')
arrow(ax, (ox, oy), P(62, 20), 'sujet', lw=1.2)
arrow(ax, (ox, oy), P(46, 50), 'autre', lw=1.2)
arc(14, 0, 20, 'sujet'); arc(22, 0, 50, 'autre'); arc(30, 20, 50, 'varie')
disc(ax, ox, oy, 1.2, 'encre')
text(ax, *P(66, 20), 'arbre', 'sujet', 's', ha='left')
text(ax, *P(49, 52), 'clocher', 'autre', 's', ha='left', va='bottom')
text(ax, 25, oy - 4, r'$\alpha$ = 20°', 'sujet', 's')
text(ax, 25, oy + 15.5, r'$\beta$ = 50°', 'autre', 's')
text(ax, 36, oy + 20, r'$\beta - \alpha$ = 30°', 'varie', 's')
box(ax, 2, 2, 25, 8, 'fixe', label='0,7660 × 0,9397', size='s')
text(ax, 31, 6, '−', 'encre', 'm')
box(ax, 35, 2, 25, 8, 'fixe', label='0,6428 × 0,3420', size='s')
box(ax, 64, 2, 22, 8, 'resultat', label='≈ 0,5 = sin 30°', size='s')
save(fig, '34-187')
