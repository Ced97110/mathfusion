import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')

fig, ax = canvas(72)
f = lambda t: 3 + 2*np.cos(t)
cx, cy, u = 12, 46, 5
pc(ax, f, 0, 2*np.pi, cx, cy, u, 'autre', 1.4)
disc(ax, cx - 1*u, cy, 1.0, 'sujet')
tq = np.arccos(-0.9)
disc(ax, cx + f(tq)*np.cos(tq)*u, cy + f(tq)*np.sin(tq)*u, 1.0, 'varie')
text(ax, 24, 68, 'r = 3 + 2 cos θ', 'autre', 'm')
box(ax, 46, 50, 40, 15, 'sujet', r=1.2)
text(ax, 66, 62, 'point d’angle π', 'sujet', 's')
text(ax, 66, 57, 'r = 3 − 2 = 1', 'encre', 's')
text(ax, 66, 52.5, 'x = −1', 'encre', 's')
box(ax, 46, 30, 40, 18, 'varie', r=1.2)
text(ax, 66, 44.5, 'voisin : cos θ = −0,9', 'varie', 's')
text(ax, 66, 39.5, 'r = 3 − 1,8 = 1,2', 'encre', 's')
text(ax, 66, 34.5, 'x = 1,2 × (−0,9) = −1,08', 'encre', 's')
f2 = numberline(ax, 12, 72, 12, -1.2, -0.9, step=0.1, arrow_right=False)
disc(ax, f2(-1.0), 16, 1.0, 'sujet'); disc(ax, f2(-1.08), 16, 1.0, 'varie')
arrow(ax, (f2(-1.0) - 1.5, 20.5), (f2(-1.08) + 1.5, 20.5), 'varie', lw=0.9)
text(ax, (f2(-1.0) + f2(-1.08))/2, 25, 'plus à gauche', 'varie', 's')
save(fig, '40-069')
