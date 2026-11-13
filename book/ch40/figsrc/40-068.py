import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
d2r = np.pi / 180
a, b = 3, 2
f = lambda t: a + b * np.cos(t)
def pc(ax, t0, t1, cx, cy, u, role='sujet', lw=1.4, n=600):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u * r * np.cos(t), cy + u * r * np.sin(t), color=COL[role], lw=lw, zorder=3, solid_capstyle='round')
pp = lambda cx, cy, u, r, t: (cx + u * r * np.cos(t), cy + u * r * np.sin(t))

fig, ax = canvas(68)
cx, cy, u = 10, 34, 6.5
pc(ax, 0, 2 * np.pi, cx, cy, u)
disc(ax, cx, cy, 0.7, 'encre')
text(ax, cx + 2.5, cy - 4, 'O', 'encre', 's')
tq = np.arccos(-0.9)
box(ax, cx - 9, cy - 7, 9, 14, 'fixe', fill=False, dash=True, lw=0.7, r=0.5)
disc(ax, *pp(cx, cy, u, f(np.pi), np.pi), 0.9, 'sujet')
disc(ax, *pp(cx, cy, u, f(tq), tq), 0.9, 'varie')
disc(ax, *pp(cx, cy, u, f(-tq), -tq), 0.9, 'varie')
text(ax, 24, 63, 'r = 3 + 2 cos θ', 'sujet', 'm')
text(ax, 24, 6, 'a = 3, b = 2 : 3 < 4', 'encre', 's')
# zoom near theta = 180 degrees
S = 36
zx, zy = 62, 34
t = np.linspace(150 * d2r, 210 * d2r, 300); r = f(t)
ax.plot(zx + S * (r * np.cos(t) + 1), zy + S * r * np.sin(t), color=COL['sujet'], lw=1.4, zorder=3)
line(ax, [(zx, zy - 22), (zx, zy + 22)], 'fixe', dash=True)
xq = f(tq) * np.cos(tq); yq = f(tq) * np.sin(tq)
disc(ax, zx, zy, 0.9, 'sujet')
disc(ax, zx + S * (xq + 1), zy + S * yq, 0.9, 'varie')
text(ax, zx + 5, zy + 12.5, 'cos θ = −0,9', 'varie', 's', ha='left')
text(ax, zx + 5, zy + 8.5, 'x = −1,08', 'varie', 's', ha='left')
text(ax, zx + 5, zy + 1.5, 'θ = 180°', 'sujet', 's', ha='left')
text(ax, zx + 5, zy - 2.5, 'x = −1', 'sujet', 's', ha='left')
text(ax, 66, 63, 'agrandi près de 180°', 'encre', 's')
save(fig, '40-068')
