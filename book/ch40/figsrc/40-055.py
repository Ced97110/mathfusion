import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

fig, ax = canvas(64)
cx, cy, u = 26, 32, 11
ax.add_patch(Circle((cx, cy), 2*u, ec=COL['fixe'], fc='none', lw=0.8, ls='--', zorder=1))
pc(ax, lambda t: 2*np.cos(3*t), 0, 2*np.pi, cx, cy, u, 'sujet', 1.3)
for k in range(3):
    x, y = pp(cx, cy, u, 2, k*2*np.pi/3)
    disc(ax, x, y, 0.9, 'resultat')
e = pp(cx, cy, u, 2, 60*d2r)
arrow(ax, (cx, cy), e, 'varie', lw=1.0)
text(ax, cx + 1.5, cy + 12.5, 'r = 2', 'varie', 's')
disc(ax, cx, cy, 0.6, 'encre')
text(ax, cx + 3.2, cy - 5, 'O', 'encre', 's')
text(ax, cx, 4.5, 'cercle de rayon 2', 'fixe', 's')
text(ax, 69, 58, 'r = 2 cos 3θ', 'sujet', 'm')
box(ax, 52, 42, 34, 9, 'fixe', label='−1 ≤ cos 3θ ≤ 1', size='s')
arrow(ax, (69, 42), (69, 36), 'varie')
text(ax, 77, 39, '× 2', 'varie', 's')
box(ax, 52, 27, 34, 9, 'sujet', label='−2 ≤ r ≤ 2', size='s')
arrow(ax, (69, 27), (69, 21), 'varie')
box(ax, 52, 12, 34, 9, 'resultat', label='|r| ≤ 2', size='m')
save(fig, '40-055')
