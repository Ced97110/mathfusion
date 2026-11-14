import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

fig, ax = canvas(80)
cx, cy, u = 30, 46, 18
f = lambda t: np.cos(2*t)
for c in (0, 180):
    t = np.linspace((c - 45)*d2r, (c + 45)*d2r, 200); r = f(t)
    poly(ax, list(zip(cx + u*r*np.cos(t), cy + u*r*np.sin(t))), 'sujet', lw=1.2)
t = np.linspace(45*d2r, 135*d2r, 200); r = f(t)
poly(ax, list(zip(cx + u*r*np.cos(t), cy + u*r*np.sin(t))), 'varie', lw=1.6)
g = pp(cx, cy, u, 1, 90*d2r); h = pp(cx, cy, u, 1, 270*d2r)
disc(ax, g[0], g[1], 1.1, 'varie', fill=False, lw=1.0)
arrow(ax, (cx, cy + 15), (cx, cy - 15), 'varie', lw=0.9)
disc(ax, cx, cy, 0.6, 'encre')
text(ax, g[0], g[1] + 5, 'θ = 90°', 'varie', 's')
text(ax, h[0], h[1] - 5, '90° + π = 270°', 'varie', 's')
x, y = pp(cx, cy, u, 1.3, 0); text(ax, x, y, '0°', 'sujet', 's')
x, y = pp(cx, cy, u, 1.3, 180*d2r); text(ax, x, y, '180°', 'sujet', 's')
box(ax, 58, 44, 28, 12, 'resultat', label='1 + n = 3 impair', size='s')
text(ax, 72, 34, 'n = 2', 'encre', 'm')
text(ax, 44, 10, 'π/2 + π = 3π/2 : place libre', 'encre', 's')
save(fig, '40-061')
