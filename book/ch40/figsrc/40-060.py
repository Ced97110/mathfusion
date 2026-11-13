import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

fig, ax = canvas(82)
cx, cy, u = 26, 50, 18
f = lambda t: np.cos(3*t)
pc(ax, f, 30*d2r, 90*d2r, cx, cy, u, 'varie', 2.6, z=3)
for c in (0, 120, 240):
    t = np.linspace((c - 30)*d2r, (c + 30)*d2r, 200); r = f(t)
    poly(ax, list(zip(cx + u*r*np.cos(t), cy + u*r*np.sin(t))), 'sujet', lw=1.2)
g = pp(cx, cy, u, 1, 60*d2r); h = pp(cx, cy, u, 1, 240*d2r)
disc(ax, g[0], g[1], 1.1, 'varie', fill=False, lw=1.0)
arrow(ax, (g[0] - 1.0*np.cos(60*d2r), g[1] - 1.0*np.sin(60*d2r)), (h[0] + 1.2*np.cos(60*d2r), h[1] + 1.2*np.sin(60*d2r)), 'varie', lw=0.9)
disc(ax, cx, cy, 0.6, 'encre')
text(ax, g[0] + 7, g[1] + 5, 'θ = 60°', 'varie', 's')
text(ax, h[0] - 1, h[1] - 6, '60° + π = 240°', 'varie', 's')
x, y = pp(cx, cy, u, 1.3, 0); text(ax, x, y, '0°', 'sujet', 's')
x, y = pp(cx, cy, u, 1.28, 120*d2r); text(ax, x, y + 1, '120°', 'sujet', 's')
box(ax, 52, 46, 34, 12, 'resultat', label='1 + n = 4 est pair', size='s')
text(ax, 69, 38, 'n = 3', 'encre', 'm')
text(ax, 44, 12, 'π/3 + π = 4π/3 = 2 × 2π/3', 'encre', 's')
save(fig, '40-060')
