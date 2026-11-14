import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(68)
def reg(cx, cy, r, n, role):
    poly(ax, [(cx + r * math.sin(2 * math.pi * k / n), cy + r * math.cos(2 * math.pi * k / n)) for k in range(n)], role)
box(ax, 2, 18, 50, 48, 'fixe', fill=False, dash=True)
box(ax, 54, 18, 32, 48, 'fixe', fill=False, dash=True)
text(ax, 27, 61, r'polygone à $n$ côtés', 'sujet', 'm', weight='bold')
text(ax, 70, 61, 'quadrature', 'autre', 'm', weight='bold')
text(ax, 70, 57, 'du cercle', 'autre', 'm', weight='bold')
reg(14, 41, 9.5, 7, 'limite'); reg(40, 41, 9.5, 17, 'resultat')
text(ax, 14, 26, '7 côtés : non', 'limite', 's'); text(ax, 40, 26, '17 côtés : oui', 'resultat', 's')
disc(ax, 70, 42, 8, 'autre', fill=False); s = 8 * math.sqrt(math.pi) / 2
poly(ax, [(70 - s, 42 - s), (70 + s, 42 - s), (70 + s, 42 + s), (70 - s, 42 + s)], 'autre', fill=False)
text(ax, 70, 26, r'même aire, lié à $\pi$', 'autre', 's')
arrow(ax, (27, 17), (27, 12), 'varie', lw=1.2); arrow(ax, (70, 17), (70, 12), 'varie', lw=1.2)
box(ax, 2, 1, 84, 10, 'varie', label='le chapitre 66 règle les deux', size='s')
save(fig, '61-252')
