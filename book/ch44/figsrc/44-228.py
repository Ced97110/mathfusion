import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(56)
for cx, sg in ((22, 1), (66, -1)):
    P = [pol(cx, 30, 11, (45 + 90 * k) if sg == 1 else (135 - 90 * k)) for k in range(4)]
    poly(ax, P, 'sujet')
    for k in range(4):
        x, y = pol(cx, 30, 7, (45 + 90 * k) if sg == 1 else (135 - 90 * k)); text(ax, x, y, str(k + 1), 'sujet', 's')
    if sg == 1: arrow(ax, pol(cx, 30, 15.5, 62), pol(cx, 30, 15.5, 118), 'varie', curve=0.3)
    else: arrow(ax, pol(cx, 30, 15.5, 118), pol(cx, 30, 15.5, 62), 'varie', curve=-0.3)
line(ax, [(44, 8), (44, 50)], 'fixe', dash=True)
arrow(ax, (38, 30), (50, 30), 'fixe', both=True)
text(ax, 44, 53, 'axe de $s$', 'fixe', 's')
text(ax, 22, 11, r'$r$', 'varie', 'l'); text(ax, 22, 5, 'sens direct', 'varie', 's')
text(ax, 66, 11, r'$srs = r^{-1}$', 'resultat', 'm'); text(ax, 66, 5, 'sens inverse', 'resultat', 's')
save(fig, '44-228')
