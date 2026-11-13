import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(70)
text(ax, 44, 64, r'$n \times 0 = 3$ ?', 'limite', 'l')
for y, a in [(48, '1'), (36, '100'), (24, '3')]:
    box(ax, 10, y, 40, 8, 'fixe', label=rf'${a} \times 0 = 0$')
    text(ax, 64, y + 4, r'$\neq 3$', 'limite', 'm')
box(ax, 10, 6, 68, 10, 'limite', label='aucun nombre ne donne 3')
save(fig, '06-028')
