import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))

fig, ax = canvas(68)
cy = 34
R = 15.5
lx = 22
ax.add_patch(Circle((lx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, ls='--', zorder=1))
pc(ax, lambda t: np.cos(3*t), 0, 2*np.pi, lx, cy, R, 'autre', 1.4)
text(ax, lx, 64, '|r| ≤ a', 'autre', 'm')
text(ax, lx, 10, 'tient dans le cercle', 'resultat', 's')
sx, u = 62, 1.55
ax.add_patch(Circle((sx, cy), 10*u, ec=COL['fixe'], fc='none', lw=0.8, ls='--', zorder=1))
pc(ax, lambda t: 0.5*t, 0, 20, sx, cy, u, 'sujet', 1.4, n=1500)
pc(ax, lambda t: 0.5*t, 20, 28, sx, cy, u, 'varie', 1.4, n=800)
p = pp(sx, cy, u, 10, 20)
disc(ax, p[0], p[1], 1.0, 'varie')
text(ax, 76, 58, 'θ = 20 : r = 10', 'varie', 's')
line(ax, [(p[0] + 1, p[1] + 1), (71, 56.5)], 'varie', lw=0.5)
text(ax, sx, 64, 'r = 0,5 θ', 'sujet', 'm')
text(ax, sx, 7, 'sort du cercle de rayon 10', 'varie', 's')
save(fig, '40-081')
