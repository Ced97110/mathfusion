import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pc(ax, f, t0, t1, cx, cy, u, role='sujet', lw=1.0, dash=False, n=600, z=3):
    t = np.linspace(t0, t1, n); r = f(t)
    ax.plot(cx + u*r*np.cos(t), cy + u*r*np.sin(t), color=COL[role], lw=lw, ls='--' if dash else '-', zorder=z, solid_capstyle='round')

fig, ax = canvas(68)
R = 12
for cx, role, tit in ((22, 'sujet', 'θ de 0° à 180°'), (66, 'varie', 'θ de 180° à 360°')):
    ox = cx - R; cy = 38
    pc(ax, lambda t: 2*R*np.cos(t)/R*0.5*np.ones_like(t), 0, 2*np.pi, ox, cy, R*2, role, 1.4)
    arrow(ax, (cx + 3, cy + R + 2), (cx - 3, cy + R + 2), role, lw=0.9)
    arrow(ax, (cx - 3, cy - R - 2), (cx + 3, cy - R - 2), role, lw=0.9)
    disc(ax, ox, cy, 0.8, 'encre'); disc(ax, ox + 2*R, cy, 0.8, 'encre')
    text(ax, ox + 3.5, cy - 3, 'O', 'encre', 's')
    text(ax, ox + 2*R - 3.5, cy - 3, '1', 'encre', 's')
    text(ax, cx, 62, tit, role, 'm')
text(ax, 44, 44, '=', 'encre', 'l')
text(ax, 44, 65, 'r = cos θ  (n = 1)', 'sujet', 's')
box(ax, 14, 6, 60, 10, 'resultat', label='un seul cercle, tracé 2 fois', size='m')
save(fig, '40-062')
