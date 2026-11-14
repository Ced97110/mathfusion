import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle

assert 26 * 12 == 312 and 312 / 0.001 == 312000

fig, ax = canvas(66)
s = 0.2
ax.add_patch(Rectangle((4, 54), 26 * s, 6, fc=FILL['sujet'], ec=COL['sujet'], lw=0.6, zorder=2))
text(ax, 4 + 26 * s + 2, 57, '26 clés (César)', 'sujet', 's', ha='left')
ax.add_patch(Rectangle((4, 40), 312 * s, 6, fc=FILL['varie'], ec=COL['varie'], lw=0.6, zorder=2))
text(ax, 4 + 312 * s + 2, 43, '312 clés', 'varie', 's', ha='left')
brace(ax, 4, 4 + 312 * s, 38, 'varie', label=r'$312 = 12 \times 26$ : 12 fois plus', down=True)
box(ax, 2, 4, 41, 14, 'fixe', label='élève :\n26 clés en 1 minute', size='s')
box(ax, 45, 4, 41, 14, 'varie', label='ordinateur : 312 clés\nen 0,001 s', size='s')
save(fig, '53-062')
