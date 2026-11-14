import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
c = (30, 36)
def arm(k, R=21, r=7):
    a = math.radians(90 + 72 * k); 
    p = lambda ang, rad: (c[0] + rad * math.cos(math.radians(ang)), c[1] + rad * math.sin(math.radians(ang)))
    return [c, p(90 + 72 * k - 20, r), p(90 + 72 * k, R), p(90 + 72 * k + 20, r)]
for k in range(5): poly(ax, arm(k), 'varie' if k == 0 else 'sujet')
pts = [(c[0] + 25 * math.cos(math.radians(a)), c[1] + 25 * math.sin(math.radians(a))) for a in range(92, 160, 4)]
line(ax, pts, 'varie', lw=1.1); arrow(ax, pts[-2], pts[-1], 'varie')
text(ax, 68, 52, 'un cinquième de tour', 'varie', 's'); text(ax, 68, 44, '72°', 'varie', 'l')
text(ax, 68, 30, '5 × 72° = 360°', 'resultat', 'm'); text(ax, 68, 23, 'tour complet', 'resultat', 's')
save(fig, '74-012')
