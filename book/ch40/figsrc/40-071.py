import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

fig, ax = canvas(64)
u = 11
lx, ly = 12, 28
rx, ry = 62, 26
pc(ax, lambda t: 1 + np.cos(t), 0, 2*np.pi, lx, ly, u, 'autre', 1.4)
pc(ax, lambda t: 1 + np.sin(t), 0, 2*np.pi, rx, ry, u, 'sujet', 1.4)
disc(ax, lx, ly, 0.7, 'encre'); disc(ax, rx, ry, 0.7, 'encre')
a = pp(lx, ly, u, 2, 0); b = pp(rx, ry, u, 2, 90*d2r)
disc(ax, a[0], a[1], 1.0, 'varie'); disc(ax, b[0], b[1], 1.0, 'varie')
text(ax, a[0] - 1, a[1] + 4, 'r = 2 à 0°', 'varie', 's', ha='right')
text(ax, b[0] + 3, b[1] + 1, 'r = 2 à 90°', 'varie', 's', ha='left')
arrow(ax, (a[0] + 1, a[1] + 4), (b[0] - 4, b[1] + 1.5), 'varie', lw=1.0, curve=0.35)
text(ax, 44, 58, 'quart de tour (π/2)', 'varie', 's')
text(ax, 24, 8, 'r = 1 + cos θ', 'autre', 'm')
text(ax, 62, 4, 'r = 1 + sin θ', 'sujet', 'm')
save(fig, '40-071')
