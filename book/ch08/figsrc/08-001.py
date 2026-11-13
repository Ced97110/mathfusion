import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig, ax = canvas(64)
x0, x1 = 8, 80
text(ax, 44, 59, r'$2+\frac{35}{100}$ mètres', 'sujet', 'l')
f = numberline(ax, x0, x1, 42, 0, 3, arrow_right=False)
ax.add_patch(Rectangle((f(0), 44), f(2) - f(0), 3, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
ax.add_patch(Rectangle((f(2), 44), f(2.35) - f(2), 3, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
text(ax, f(1), 50, '2 mètres entiers', 'sujet', 's')
text(ax, f(2.175), 50, '35 centièmes', 'varie', 's')
zx0, zx1, zy0, zy1 = 8, 80, 14, 22
for xe in (f(2), f(3)):
    pass
line(ax, [(f(2), 35), (zx0, zy1 + 1)], 'fixe', dash=True)
line(ax, [(f(3), 35), (zx1, zy1 + 1)], 'fixe', dash=True)
step = (zx1 - zx0) / 100
ax.add_patch(Rectangle((zx0, zy0), 35 * step, zy1 - zy0, ec='none', fc=FILL['varie'], zorder=1.5))
for i in range(101):
    ax.plot([zx0 + i * step] * 2, [zy0, zy1], color=COL['varie'] if i <= 35 else COL['fixe'], lw=0.25, zorder=2)
line(ax, [(zx0, zy0), (zx1, zy0), (zx1, zy1), (zx0, zy1), (zx0, zy0)], 'fixe', lw=0.8)
text(ax, zx0 + 35 * step / 2, (zy0 + zy1) / 2, '35 parts', 'varie', 's')
text(ax, 44, 8, '1 mètre = 100 parts égales', 'fixe', 's')
save(fig, '08-001')
