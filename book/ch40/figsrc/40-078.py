import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))

fig, ax = canvas(70)
cx, cy, u = 26, 38, 7
pc(ax, lambda t: 0.5*t, 0, 2*np.pi, cx, cy, u, 'sujet', 1.5)
disc(ax, cx, cy, 0.7, 'encre')
for th in (1, 2, 4):
    p = pp(cx, cy, u, 0.5*th, th)
    disc(ax, p[0], p[1], 0.9, 'varie')
    q = pp(cx, cy, u, 0.5*th + 0.75, th)
    text(ax, q[0], q[1], str(th), 'varie', 's')
text(ax, cx, 66, 'r = aθ : grandit avec θ', 'sujet', 'm')
text(ax, cx, 10, 'a = 0,5', 'encre', 's')
text(ax, cx, 5, 'θ = 1, 2, 4 → r = 0,5 ; 1 ; 2', 'varie', 's')
ox, oy = 70, 52
ax.add_patch(Circle((ox, oy), 8, ec=COL['autre'], fc='none', lw=1.4, zorder=3))
text(ax, ox, 40, 'r = a : reste a', 'autre', 's')
pc(ax, lambda t: np.cos(3*t), 0, 2*np.pi, 70, 24, 8, 'autre', 1.4)
text(ax, 70, 10, 'r = a cos nθ : oscille', 'autre', 's')
save(fig, '40-078')
