import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(58)
x0, x1, yb, hh = 12, 80, 10, 30
X = lambda t: x0 + t / (2 * math.pi) * (x1 - x0)
Y = lambda v: yb + v * hh
ts = [i * 2 * math.pi / 400 for i in range(401)]
ax.plot([X(t) for t in ts], [Y(math.cos(t) ** 2) for t in ts], color=COL['sujet'], lw=6, alpha=0.35, solid_capstyle='round', zorder=2)
ax.plot([X(t) for t in ts], [Y((1 + math.cos(2 * t)) / 2) for t in ts], color=COL['varie'], lw=1.3, ls=(0, (3, 2)), zorder=3)
line(ax, [(x0 - 3, yb), (x1 + 3, yb)], 'fixe', lw=0.7)
for t, s in ((0, '0'), (math.pi, 'π'), (2 * math.pi, '2π')):
    line(ax, [(X(t), yb - 1), (X(t), yb + 1)], 'fixe', lw=0.7); text(ax, X(t), yb - 3.5, s, 'fixe', 's')
for t, v, s in ((0, 1, '1'), (math.pi / 4, 0.5, '0,5'), (math.pi / 2, 0, '0')):
    disc(ax, X(t), Y(v), 1.1, 'resultat')
    text(ax, X(t) + 2.2, Y(v) + (2.5 if v else 3), s, 'resultat', 's', ha='left')
line(ax, [(8, 53), (16, 53)], 'sujet', lw=5); text(ax, 18, 53, r'$\cos^2 x$', 'sujet', 's', ha='left')
line(ax, [(44, 53), (52, 53)], 'varie', dash=True, lw=1.3); text(ax, 54, 53, r'$(1+\cos 2x)/2$', 'varie', 's', ha='left')
text(ax, 44, 46, '3 points : 0, 45°, 90°', 'resultat', 's')
save(fig, '34-160')
