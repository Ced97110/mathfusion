import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
y = 20
f = numberline(ax, 10, 76, y, 4, 5, step=0.1, arrow_right=False, every=5)
ax.add_patch(Rectangle((f(4), y + 0.6), f(5) - f(4), 2.0, fc=FILL['sujet'], ec=COL['sujet'], lw=0.6, zorder=2))
box(ax, f(4) - 9, y + 12, 24, 8, 'autre', label='4° : 0,0699', size='s')
box(ax, f(5) - 15, y + 12, 24, 8, 'autre', label='5° : 0,0875', size='s')
line(ax, [(f(4), y + 12), (f(4), y + 2.6)], 'autre')
line(ax, [(f(5), y + 12), (f(5), y + 2.6)], 'autre')
text(ax, 43, y + 26, '0,0833 est entre les deux', 'resultat')
for v, dy in ((4.7, 6.0), (4.8, 6.0)):
    arrow(ax, (f(v), y - 8.5), (f(v), y - 1.2), 'varie')
text(ax, f(4.7) - 1.5, y - 11, '4,7°', 'varie', 's')
text(ax, f(4.8) + 2.5, y - 11, '4,8°', 'varie', 's')
text(ax, f(4.75), y - 16, 'essais', 'varie', 's')
save(fig, '33-006')
