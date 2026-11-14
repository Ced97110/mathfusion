import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

a, b = 1.5, 1.0
f = lambda t: a + b*np.cos(t)
fig, ax = canvas(66)
# main curve
cx, cy, u = 14, 33, 11
pc(ax, f, 0, 2*np.pi, cx, cy, u, 'sujet', 1.4)
disc(ax, cx, cy, 0.7, 'encre')
text(ax, cx + 2.5, cy - 4, 'O', 'encre', 's')
tq0 = np.arccos(-0.9)
box(ax, cx - 8.5, cy - 7, 8.5, 14, 'fixe', fill=False, dash=True, lw=0.7, r=0.5)
disc(ax, cx - 0.5*u, cy, 0.9, 'sujet')
disc(ax, *pp(cx, cy, u, f(tq0), tq0), 0.9, 'varie')
disc(ax, *pp(cx, cy, u, f(-tq0), -tq0), 0.9, 'varie')
text(ax, 24, 60, 'r = 1,5 + cos θ', 'sujet', 'm')
text(ax, 24, 6, 'b < a < 2b : 1 < 1,5 < 2', 'encre', 's')
# zoom near theta = 180 deg
S = 45
zx, zy = 62, 33
t = np.linspace(140*d2r, 220*d2r, 300); r = f(t)
X = r*np.cos(t); Y = r*np.sin(t)
ax.plot(zx + S*(X + 0.5), zy + S*Y, color=COL['sujet'], lw=1.4, zorder=3)
line(ax, [(zx, zy - 22), (zx, zy + 22)], 'fixe', dash=True)
tq = np.arccos(-0.9)
rq = f(tq); xq = rq*np.cos(tq); yq = rq*np.sin(tq)
disc(ax, zx, zy, 0.9, 'sujet')
disc(ax, zx + S*(xq + 0.5), zy + S*yq, 0.9, 'varie')
text(ax, zx + 4, zy + 12.5, 'cos θ = −0,9', 'varie', 's', ha='left')
text(ax, zx + 4, zy + 8.5, 'x = −0,54', 'varie', 's', ha='left')
text(ax, zx + 4, zy + 1.5, 'θ = 180°', 'sujet', 's', ha='left')
text(ax, zx + 4, zy - 2.5, 'x = −0,5', 'sujet', 's', ha='left')
text(ax, 66, 60, 'agrandi près de 180°', 'encre', 's')
save(fig, '40-067')
