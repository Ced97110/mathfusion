import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(86)
cs = [(35, 66), (53, 66), (44, 53)]
R = 14
g = np.linspace(0, 88, 880); gy = np.linspace(0, 86, 860)
X, Y = np.meshgrid(g, gy)
m = np.ones_like(X, bool)
for cx, cy in cs: m &= (X - cx) ** 2 + (Y - cy) ** 2 < R ** 2
import matplotlib.colors as mc
img = np.zeros(m.shape + (4,)); img[m] = mc.to_rgba(COL['sujet'])
ax.imshow(img, extent=(0, 88, 0, 86), origin='lower', zorder=1, interpolation='nearest')
for cx, cy in cs:
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc=FILL['fixe'] if False else 'none', lw=0.9, zorder=3))
ax.set_xlim(0, 88); ax.set_ylim(0, 86)
text(ax, 27, 72, r'$A_1$', 'fixe', 'm')
text(ax, 61, 72, r'$A_2$', 'fixe', 'm')
text(ax, 44, 44, r'$A_3$', 'fixe', 'm')
text(ax, 44, 34, r'$n = 3$ clubs', 'encre', 'm')
text(ax, 44, 24, r'$A_1 \cap A_2 \cap \cdots \cap A_n$', 'varie', 'm')
arrow(ax, (44, 21), (44, 17), 'varie')
text(ax, 44, 9, r'$\bigcap_{i=1}^{n} A_i$', 'sujet', 'l')
save(fig, '42-138')
