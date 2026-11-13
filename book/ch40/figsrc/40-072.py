import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')

fig, ax = canvas(64)
u, cy = 18, 36
cx = 22
pc(ax, lambda t: np.cos(2*t), 0, 2*np.pi, cx, cy, u, 'autre', 1.4)
disc(ax, cx, cy, 0.7, 'encre')
text(ax, cx, 59, 'r = cos 2θ', 'autre', 'm')
text(ax, cx, 14, 'rosace : 4 pétales', 'autre', 's')
cx = 66
th = np.linspace(-np.pi/4, np.pi/4, 500)
for sgn in (1, -1):
    ax.plot(cx + u*sgn*np.sqrt(np.cos(2*th))*np.cos(th), cy + u*sgn*np.sqrt(np.cos(2*th))*np.sin(th), color=COL['sujet'], lw=1.4, zorder=3)
disc(ax, cx, cy, 0.7, 'encre')
text(ax, cx + 2.5, cy + 3, 'O', 'encre', 's')
text(ax, cx, 59, 'r² = cos 2θ', 'sujet', 'm')
text(ax, cx, 14, '2 boucles qui se croisent', 'sujet', 's')
text(ax, 66, 6, 'lemniscate de Bernoulli', 'resultat', 's')
save(fig, '40-072')
