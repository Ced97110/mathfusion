import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
text(ax, 24, 57, r'$\mathbb{Z}/2\mathbb{Z}$ : deux heures', 'sujet', 's', weight='bold')
cx, cy, r = 24, 30, 15
ax.add_patch(Circle((cx, cy), r, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
p0 = (cx, cy + r); p1 = (cx, cy - r)
disc(ax, *p0, 4, 'sujet', label='0')
disc(ax, *p1, 4, 'sujet', label='1')
arrow(ax, (p0[0] + 4.5, p0[1] - 1), (p1[0] + 4.5, p1[1] + 1), 'varie', lw=1.5, curve=-0.55)
arrow(ax, (p1[0] - 4.5, p1[1] + 1), (p0[0] - 4.5, p0[1] - 1), 'varie', lw=1.5, curve=-0.55)
text(ax, cx + r + 3, cy, r'$+1$', 'varie', 's')
text(ax, cx - r - 3, cy, r'$+1$', 'varie', 's')
box(ax, 54, 42, 32, 9, 'resultat', label=r'$2\cdot1=0$', size='s')
box(ax, 54, 29, 32, 9, 'fixe', label=r'$2\neq0$', size='s')
box(ax, 54, 16, 32, 9, 'fixe', label=r'$1\neq0$', size='s')
box(ax, 54, 3, 32, 9, 'limite', label='règle 4 : fausse', size='s')
save(fig, '58-116')
