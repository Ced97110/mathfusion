import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

fig, ax = canvas(64)
cx, cy, u = 14, 33, 13
f = lambda t: 1 + 2*np.cos(t)
line(ax, [(cx - 5, cy), (cx + 3.3*u, cy)], 'fixe', lw=0.4)
pc(ax, f, -120*d2r, 120*d2r, cx, cy, u, 'sujet', 1.4)
pc(ax, f, 120*d2r, 240*d2r, cx, cy, u, 'varie', 1.6)
disc(ax, cx, cy, 0.7, 'encre')
text(ax, cx - 1.5, cy - 4, 'O', 'encre', 's')
p3 = pp(cx, cy, u, 3, 0); p1 = pp(cx, cy, u, 1, 0)
disc(ax, p3[0], p3[1], 1.0, 'sujet'); disc(ax, p1[0], p1[1], 1.0, 'varie')
text(ax, p3[0] + 3, cy + 4, 'θ = 0° : r = 3', 'sujet', 's', ha='left')
text(ax, 60, 16, 'θ = 180° : r = −1', 'varie', 's')
arrow(ax, (50, 18.5), (p1[0] + 1.2, p1[1] - 1.2), 'varie', lw=0.8, curve=-0.2)
text(ax, 44, 60, 'r = 1 + 2 cos θ', 'sujet', 'm')
text(ax, 72, 50, 'a = 1 < b = 2', 'encre', 's')
text(ax, 34, 5, 'cos θ < −1/2 : r < 0', 'varie', 's')
save(fig, '40-065')
