import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))

fig, ax = canvas(66)
u, cy = 9, 33
for ox, f, role, eq, n1, n2 in ((8, lambda t: 1 + np.cos(t), 'sujet', 'r = 1 + cos θ', 'a = b : r = 0 en O', 'pointe au pôle'),
                                (52, lambda t: 2 + np.cos(t), 'autre', 'r = 2 + cos θ', 'a = 2, b = 1 : r ≥ 1', 'pas de pointe')):
    pc(ax, f, 0, 2*np.pi, ox, cy, u, role, 1.4)
    disc(ax, ox, cy, 1.0, 'encre')
    mid = ox + (10 if role == 'sujet' else 18)
    text(ax, mid, 58, eq, role, 'm')
    text(ax, mid, 11, n1, 'encre', 's')
    text(ax, mid, 5.5, n2, role, 's')
    text(ax, ox - 0.5, cy - 4, 'O', 'encre', 's')
save(fig, '40-066')
