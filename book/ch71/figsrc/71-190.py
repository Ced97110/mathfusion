import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Ellipse
fig, ax = canvas(46)
w_, g = 18.5, 3.0
names = ['ellipse', '2 branches', 'deux droites', 'vide']
signs = ['(+, +)', '(+, −)', '(+, 0)', '(−, −)']
text(ax, 44, 42, '$Q=1$', 'encre', 's')
for i in range(4):
    x = 2.5 + i * (w_ + g); cx, cy = x + w_ / 2, 22
    box(ax, x, 10, w_, 26, 'fixe', fill=False, lw=0.6)
    text(ax, cx, 38.8, signs[i], 'encre', 's')
    text(ax, cx, 6, names[i], 'sujet' if i < 3 else 'limite', 's')
    line(ax, [(x + 1.5, cy), (x + w_ - 1.5, cy)], 'fixe', lw=0.4); line(ax, [(cx, 11.5), (cx, 34.5)], 'fixe', lw=0.4)
    if i == 0:
        ax.add_patch(Ellipse((cx, cy), 14, 8, ec=COL['sujet'], fc=FILL['sujet'], lw=1.2, zorder=2))
    if i == 1:
        line(ax, [(x + 2, cy - 9), (x + w_ - 2, cy + 9)], 'varie', dash=True, lw=0.6)
        line(ax, [(x + 2, cy + 9), (x + w_ - 2, cy - 9)], 'varie', dash=True, lw=0.6)
        for sg in (1, -1):
            line(ax, [(cx + sg * 3.5 * math.cosh(t / 10), cy + 3.5 * math.sinh(t / 10)) for t in range(-12, 13)], 'sujet', lw=1.2)
    if i == 2:
        for sg in (1, -1): line(ax, [(cx + sg * 4, 12), (cx + sg * 4, 32)], 'sujet', lw=1.2)
save(fig, '71-190')
