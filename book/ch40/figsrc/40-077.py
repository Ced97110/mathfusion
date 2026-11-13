import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

fig, ax = canvas(64)
cx, cy, u = 30, 32, 26
th = np.linspace(-np.pi/4, np.pi/4, 600)
for sgn in (1, -1):
    ax.plot(cx + u*sgn*np.sqrt(np.cos(2*th))*np.cos(th), cy + u*sgn*np.sqrt(np.cos(2*th))*np.sin(th), color=COL['sujet'], lw=1.4, zorder=3)
for a in (45, -45):
    line(ax, [pp(cx, cy, 1, -28, a*d2r), pp(cx, cy, 1, 28, a*d2r)], 'fixe', lw=0.6, dash=True)
text(ax, cx + 22, cy + 24, '45°', 'fixe', 's')
text(ax, cx + 22, cy - 24, '−45°', 'fixe', 's')
pts = [(40, 'varie', 'θ = 40° : r ≈ 0,42', 0.4167), (44, 'varie', 'θ = 44° : r ≈ 0,19', 0.187)]
for deg, role, lab, r in pts:
    p = pp(cx, cy, u, r, deg*d2r)
    disc(ax, p[0], p[1], 0.9, role)
disc(ax, cx, cy, 1.0, 'resultat')
text(ax, 70, 44, 'θ = 40° : r ≈ 0,42', 'varie', 's')
text(ax, 70, 36, 'θ = 44° : r ≈ 0,19', 'varie', 's')
text(ax, 70, 28, 'θ = 45° : r = 0', 'resultat', 's')
p40 = pp(cx, cy, u, 0.4167, 40*d2r); p44 = pp(cx, cy, u, 0.187, 44*d2r)
line(ax, [(p40[0] + 1, p40[1] + 0.5), (53, 44.5)], 'varie', lw=0.5)
line(ax, [(p44[0] + 1, p44[1]), (53, 36.5)], 'varie', lw=0.5)
line(ax, [(cx + 1, cy - 0.5), (54, 28.5)], 'resultat', lw=0.5)
text(ax, cx, 5, 'r² = cos 2θ : la courbe arrive en O', 'sujet', 's')
save(fig, '40-077')
