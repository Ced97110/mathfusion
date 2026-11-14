import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

cx, cy, s = 44, 38, 26
fig, ax = canvas(82)
box(ax, 2, 2, 84, 78, 'fixe', fill=True, label=None, r=1.5)
text(ax, 5, 75, r'$\mathbb{C}$ sans 0 : tous les complexes non nuls', 'fixe', 's', ha='left')
disc(ax, cx, cy, s, 'encre', fill=True, lw=0.0)
disc(ax, cx, cy, s, 'sujet', fill=False, lw=1.4)
arrow(ax, (6, cy), (82, cy), 'fixe', lw=0.6)
arrow(ax, (cx, 6), (cx, 68), 'fixe', lw=0.6)
A = (0.6, 0.8)
B = (math.cos(math.radians(60)), math.sin(math.radians(60)))
for (p, lab, dx, dy, ha) in [(A, r'$\frac{3}{5}+\frac{4}{5}\,i$', 3, -3.5, 'left'), (B, r'$\mathrm{cis}\,60°$', -2.5, 3.5, 'right')]:
    line(ax, [(cx, cy), (cx + p[0] * s, cy + p[1] * s)], 'sujet', lw=0.7, dash=True)
    disc(ax, cx + p[0] * s, cy + p[1] * s, 1.4, 'sujet')
    text(ax, cx + p[0] * s + dx, cy + p[1] * s + dy, lab, 'sujet', 's', ha=ha)
text(ax, cx - 15, cy - 12, r'$\mathbb{T}$ : module 1', 'sujet', 'm')
text(ax, cx, 10, r'$1\times 1=1$ : le produit reste dans $\mathbb{T}$', 'resultat', 's')
save(fig, '39-105')
