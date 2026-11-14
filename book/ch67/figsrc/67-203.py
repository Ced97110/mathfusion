import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cx, cy, R = 32, 46, 26
line(ax, [(3, cy), (61, cy)], 'fixe')
line(ax, [(cx, 18), (cx, 75)], 'fixe')
disc(ax, cx, cy, R, 'sujet', fill=False, lw=1.1)
px, py = cx + 0.6 * R, cy + 0.8 * R
line(ax, [(px, cy), (px, py)], 'varie', dash=True)
line(ax, [(cx, py), (px, py)], 'varie', dash=True)
disc(ax, px, py, 1.6, 'resultat')
text(ax, 64, cy, '$a$', 'fixe', 'm')
text(ax, cx + 3.5, 77, '$b$', 'fixe', 'm')
text(ax, px, cy - 4.5, r'$\frac{3}{5}$', 'varie', 'm')
text(ax, cx - 2.5, py, r'$\frac{4}{5}$', 'varie', 'm', ha='right')
text(ax, px + 3, py + 5, r'$\frac{3}{5}+\frac{4}{5}i$', 'resultat', 'm', ha='left')
text(ax, 72, 32, r'$a^{2}+b^{2}=1$', 'sujet', 'm')
text(ax, 44, 8, r'tout point rationnel : $v/\bar{v}$', 'encre', 'm')
save(fig, '67-203')
