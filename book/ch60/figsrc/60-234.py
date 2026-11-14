import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(84)
text(ax, 44, 78, r'$\mathbb{Z}$ : une infinité d’éléments', 'sujet', 'm', weight='bold')
f = numberline(ax, 20, 68, 66, -2, 2, arrow_right=False, role='sujet')
arrow(ax, (20, 66), (10, 66), 'sujet')
arrow(ax, (68, 66), (78, 66), 'sujet')
cx, cy, R = 22, 30, 10
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
for k in range(4):
    a = math.pi / 2 - k * math.pi / 2
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 3.4, 'autre', label=str(k), size='s')
text(ax, cx, 10, r'$\mathbb{Z}/4$ : 4 éléments', 'autre', 'm')
arrow(ax, (62, 55), (62, 44), 'limite')
box(ax, 44, 22, 40, 21, 'limite', dash=True,
    label='jamais une somme\nfinie de ' + r'$\mathbb{Z}/d$' + '\n(aucun ordre ' + r'$n$' + ')', size='s')
save(fig, '60-234')
