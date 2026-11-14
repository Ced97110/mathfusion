import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(72)
text(ax, 44, 66, r'$\mathbb{C}^{*}$', 'sujet', 'xl')
text(ax, 44, 59, 'complexes non nuls, avec la multiplication', 'encre', 's')
box(ax, 14, 8, 60, 46, 'sujet')
cx, cy = 44, 31
line(ax, [(16, cy), (72, cy)], 'fixe'); line(ax, [(cx, 10), (cx, 52)], 'fixe')
text(ax, 72, cy - 3, 'réels', 'fixe', 's', ha='right')
text(ax, cx + 2, 50, 'multiples de $i$', 'fixe', 's', ha='left')
disc(ax, cx, cy + 12, 1.3, 'sujet'); text(ax, cx - 3, cy + 12, '$i$', 'sujet', 'm')
disc(ax, cx, cy, 1.8, 'limite', fill=False, lw=1.1)
text(ax, cx + 3, cy - 4, '0 retiré', 'limite', 's', ha='left')
text(ax, 20, 14, r'$\mathbb{C}$ : tout le plan', 'sujet', 's', ha='left')
save(fig, '46-038')
