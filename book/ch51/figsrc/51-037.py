import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(74)
cx, cy, R = 24, 38, 15
disc(ax, cx, cy, R, 'fixe', fill=False)
P = lambda k, r=R: (cx + r * math.cos(math.radians(90 - 90 * k)), cy + r * math.sin(math.radians(90 - 90 * k)))
for k in range(4):
    p = P(k); disc(ax, p[0], p[1], 3.4, 'sujet' if k == 2 else 'fixe', label=str(k), size='s')
def arc(a0, a1, role, r=9.2):
    n = 40; pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts[:-3], role, lw=1.1); arrow(ax, pts[-4], pts[-1], role)
arc(-90 - 14, -360 + 14, 'varie'); arc(0 - 14, -90 + 14, 'resultat')
q = lambda a, r: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
text(ax, *q(135, 4.2), '+3', 'varie', 's'); text(ax, *q(-45, 4.2), '+1', 'resultat', 's')
text(ax, 46, 58, '2 + 3 = 1', 'varie', 'm', ha='left')
text(ax, 46, 48, '1 + 1 = 2', 'resultat', 'm', ha='left')
text(ax, 46, 36, '3 + 1 = 4, soit 0', 'resultat', 'm', ha='left')
text(ax, 46, 26, 'l’opposé de 3 est 1', 'resultat', 'm', ha='left', weight='bold')
text(ax, 46, 16, 'on revient en 2', 'fixe', 'm', ha='left')
save(fig, '51-037')
