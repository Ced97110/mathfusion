import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')

fig, ax = canvas(68)
cx, cy, u = 30, 32, 6.2
line(ax, [(cx, cy), (cx, cy + 28)], 'fixe', lw=0.6, dash=True)
pc(ax, lambda t: 0.5*t, 0, 8.15, cx, cy, u, 'sujet', 1.5)
disc(ax, cx, cy, 0.7, 'encre')
r1 = 0.5*(np.pi/2); r2 = 0.5*(np.pi/2 + 2*np.pi)
y1 = cy + u*r1; y2 = cy + u*r2
disc(ax, cx, y1, 1.0, 'sujet'); disc(ax, cx, y2, 1.0, 'varie')
arrow(ax, (cx, y1 + 1.5), (cx, y2 - 1.5), 'resultat', lw=1.0, both=True)
text(ax, cx, 63, 'r = 0,5 θ', 'sujet', 'm')
text(ax, 72, 54, 'passage 1', 'sujet', 's')
text(ax, 72, 49.5, 'θ ≈ 1,571 : r ≈ 0,785', 'sujet', 's')
text(ax, 72, 40, 'passage 2', 'varie', 's')
text(ax, 72, 35.5, 'θ ≈ 7,854 : r ≈ 3,927', 'varie', 's')
text(ax, 72, 26, 'écart ≈ 3,14', 'resultat', 'm')
text(ax, 72, 20.5, '= 0,5 × 6,28 = a × 2π', 'resultat', 's')
save(fig, '40-079')
