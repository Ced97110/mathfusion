import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
fig, ax = canvas(48)
text(ax, 44, 44, r'8 parts, on en prend $a$', 'encre')
for cx, a in ((16, 0), (44, 3), (72, 8)):
    for k in range(8):
        on = k < a
        ax.add_patch(Wedge((cx, 26), 11, 90 - (k + 1) * 45, 90 - k * 45, ec=COL['varie'] if on else COL['fixe'],
                           fc=FILL['varie'] if on else FILL['fixe'], lw=0.8, zorder=2))
    text(ax, cx, 8, rf'$a={a}$', 'varie')
save(fig, '06-016')
