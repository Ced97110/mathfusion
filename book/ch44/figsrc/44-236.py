import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(66)
for y, f, sg, role, lab, sens in ((46, r'$\tau_3 \circ \tau_1$', 1, 'sujet', r'$\sigma$', 'sens direct'), (14, r'$\tau_1 \circ \tau_3$', -1, 'varie', r'$\sigma^2$', 'sens inverse')):
    cx = 48
    poly(ax, pg(cx, y, 10, 3), 'fixe')
    for k, a in enumerate((90, 210, 330)):
        x, yy = pol(cx, y, 5.5, a); text(ax, x, yy - (1 if k == 0 else 0), str(k + 1), 'fixe', 's')
    if sg == 1: arrow(ax, pol(cx, y, 13, 100), pol(cx, y, 13, 200), 'sujet', curve=0.28)
    else: arrow(ax, pol(cx, y, 13, 80), pol(cx, y, 13, 340), 'varie', curve=-0.28)
    text(ax, 14, y + 2, f, role, 'l'); text(ax, 76, y + 2, lab, role, 'l'); text(ax, 76, y - 4, sens, role, 's')
text(ax, 44, 31, 'ordre inversé → sens inversé', 'resultat', 's')
save(fig, '44-236')
