import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(86)
for i, t in enumerate((r'$r^4 = 1$', r'$s^2 = 1$', r'$srs = r^{-1}$')):
    box(ax, 2, 60 - i * 15, 27, 10, 'sujet', label=t, size='m')
steps = (r'$s\,r\,r\,s$', r'$(srs)(srs)$', r'$r^{-1}\,r^{-1}$', r'$r^2$')
ys = (74, 54, 34, 12)
for i, t in enumerate(steps):
    box(ax, 40, ys[i], 26, 10, 'resultat' if i == 3 else 'fixe', label=t, size='m')
for i, t in enumerate((r'$s^2 = 1$', r'$srs = r^{-1}$', r'$r^4 = 1$')):
    arrow(ax, (53, ys[i] - 0.5), (53, ys[i + 1] + 10.5), 'varie')
    text(ax, 68, (ys[i] + ys[i + 1] + 10) / 2, t, 'varie', 's', ha='left')
text(ax, 15, 78, 'trois égalités', 'sujet', 's')
save(fig, '44-227')
