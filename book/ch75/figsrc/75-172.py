import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(74)
cx1, cx2, cy, r = 32, 56, 44, 22
n = 80
a1 = [(cx2 + r*math.cos(math.pi - 1.2*0 - t), cy + r*math.sin(t)) for t in []]
d = (cx2 - cx1) / 2; m = (cx1 + cx2) / 2
t0 = math.acos(d / r)
lens = [(cx1 + r*math.cos(-t0 + 2*t0*k/n), cy + r*math.sin(-t0 + 2*t0*k/n)) for k in range(n+1)]
lens += [(cx2 - r*math.cos(t0 - 2*t0*k/n), cy + r*math.sin(t0 - 2*t0*k/n)) for k in range(n+1)]
poly(ax, lens, 'sujet')
disc(ax, cx1, cy, r, 'fixe', fill=False, lw=1.1); disc(ax, cx2, cy, r, 'autre', fill=False, lw=1.1)
text(ax, cx1-8, cy+10, 'orthogonales', 'fixe', 's'); text(ax, cx2+8, cy+10, 'symplectiques', 'autre', 's')
text(ax, m, cy+2, r'$U(1)$', 'sujet', 'm', weight='bold'); text(ax, m, cy-4, r'= $SO(2)$', 'sujet', 'm', weight='bold')
text(ax, m, 15, 'quart de tour :', 'resultat', 's', weight='bold')
text(ax, m, 9, 'produit scalaire 0 → 0 ; aire 1 → 1', 'resultat', 's')
save(fig, '75-172')
