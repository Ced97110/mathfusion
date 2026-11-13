import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def pp(cx, cy, u, r, t): return (cx + u*r*np.cos(t), cy + u*r*np.sin(t))
d2r = np.pi/180

fig, ax = canvas(60)
cx, cy, u = 24, 30, 20
line(ax, [(cx - 22, cy), (cx + 22, cy)], 'fixe', lw=0.4)
line(ax, [(cx, cy - 22), (cx, cy + 22)], 'fixe', lw=0.4)
th = np.linspace(-np.pi/4, np.pi/4, 500)
for sgn in (1, -1):
    ax.plot(cx + u*sgn*np.sqrt(np.cos(2*th))*np.cos(th), cy + u*sgn*np.sqrt(np.cos(2*th))*np.sin(th), color=COL['sujet'], lw=1.4, zorder=3)
q = np.sqrt(0.5)
P = pp(cx, cy, u, q, 30*d2r)
Pa = (P[0], 2*cy - P[1]); Pb = (2*cx - P[0], P[1]); Pc = (2*cx - P[0], 2*cy - P[1])
disc(ax, P[0], P[1], 1.1, 'sujet')
disc(ax, Pa[0], Pa[1], 1.1, 'varie'); disc(ax, Pb[0], Pb[1], 1.1, 'autre'); disc(ax, Pc[0], Pc[1], 1.1, 'resultat')
line(ax, [P, Pa], 'varie', lw=0.6, dash=True); line(ax, [P, Pb], 'autre', lw=0.6, dash=True); line(ax, [P, Pc], 'resultat', lw=0.6, dash=True)
text(ax, P[0] + 3, P[1] + 3.5, 'P', 'sujet', 's')
rows = [('r → −r', '(−r)² = r²', 'resultat', 40),
        ('θ → −θ', 'cos(−2θ) = cos 2θ', 'varie', 30),
        ('θ → π − θ', 'cos(2π − 2θ) = cos 2θ', 'autre', 20)]
for a, b, role, y in rows:
    text(ax, 50, y + 3, a, role, 'm', ha='left')
    text(ax, 50, y - 1.2, b, role, 's', ha='left')
text(ax, 68, 54, 'trois tests réussis', 'encre', 's')
save(fig, '40-075')
