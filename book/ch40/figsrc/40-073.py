import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

fig, ax = canvas(70)
cx, cy, u, R = 28, 38, 22, 27
def wedge(a0, a1, role):
    t = np.linspace(a0*d2r, a1*d2r, 60)
    pts = [(cx, cy)] + list(zip(cx + R*np.cos(t), cy + R*np.sin(t)))
    poly(ax, pts, role, lw=0.4)
wedge(-45, 45, 'resultat'); wedge(135, 225, 'resultat')
wedge(45, 135, 'limite'); wedge(225, 315, 'limite')
th = np.linspace(-np.pi/4, np.pi/4, 500)
for sgn in (1, -1):
    ax.plot(cx + u*sgn*np.sqrt(np.cos(2*th))*np.cos(th), cy + u*sgn*np.sqrt(np.cos(2*th))*np.sin(th), color=COL['sujet'], lw=1.5, zorder=3)
p = pp(cx, cy, u, 0.707, 30*d2r)
line(ax, [(cx, cy), pp(cx, cy, R, 1, 30*d2r)], 'resultat', lw=0.9)
disc(ax, p[0], p[1], 0.9, 'resultat')
line(ax, [(cx, cy), pp(cx, cy, R, 1, 60*d2r)], 'limite', lw=0.9, dash=True)
text(ax, cx, 3.5, 'aucun point entre 45° et 135°', 'limite', 's')
text(ax, 72, 62, 'θ = 30°', 'resultat', 'm')
text(ax, 72, 56, 'cos 60° = 0,5', 'resultat', 's')
text(ax, 72, 51, 'r = ± 0,707', 'resultat', 's')
text(ax, 72, 40, 'θ = 60°', 'limite', 'm')
text(ax, 72, 34, 'cos 120° = −0,5', 'limite', 's')
text(ax, 72, 29, 'r² < 0 : impossible', 'limite', 's')
save(fig, '40-073')
