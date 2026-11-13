import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cx, cy, R = 28, 28, 19
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
line(ax, [(cx - R - 4, cy), (cx + R + 4, cy)], 'fixe', lw=0.5)
line(ax, [(cx, cy - R - 4), (cx, cy + R + 4)], 'fixe', lw=0.5)
disc(ax, cx + R, cy, 3.2, 'sujet', label='1')
text(ax, 70, 46, '$n = 1$', 'sujet', 'l')
text(ax, 70, 36, '$z^1 = 1$', 'varie', 'm')
text(ax, 70, 30, 'une seule solution', 'varie', 's')
text(ax, 70, 19, '$\\varphi(1) = 1$', 'resultat', 'm')
text(ax, 70, 13, '1 engendre {1}', 'resultat', 's')
save(fig, '46-272')
