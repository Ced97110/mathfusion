import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def gr(ax, fn, ox, oy, sx, sy, t0, t1, role, lw=1.3, n=240, dash=False):
    pts = [(ox + sx * (t0 + (t1 - t0) * i / n), oy + sy * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
def dot(ax, x, y, role, r=1.1, fill=True):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if fill else FILL["encre"], lw=0.9, zorder=6))

fig, ax = canvas(54)
K, L = 120.0, 0.1
text(ax, 22, 48, 'près du départ', 'sujet', 's'); text(ax, 66, 48, 'près du sommet', 'sujet', 's')
# left : arc from angle 0, circle centre at (bx - K, by)
bx, by = 24, 12
arc = [(bx - K + K * math.cos(L * i / 30), by + K * math.sin(L * i / 30)) for i in range(31)]
line(ax, arc, 'varie', lw=2.0)
hx = arc[-1]
line(ax, [(bx, by), (bx, hx[1])], 'resultat', lw=1.6)
text(ax, bx + 2, by + 6, 'hauteur\n0,0998', 'resultat', 's', ha='left')
text(ax, bx - 3, by + 6, 'arc\n0,1', 'varie', 's', ha='right')
# right : arc from top, circle centre at (ax0, by' - K)
ax0, ay0 = 54, 24
arc2 = [(ax0 + K * math.sin(L * i / 30), ay0 - K + K * math.cos(L * i / 30)) for i in range(31)]
line(ax, arc2, 'varie', lw=2.0)
e = arc2[-1]
line(ax, [(e[0], arc2[0][1]), (e[0], e[1])], 'resultat', lw=1.6)
line(ax, [arc2[0], (e[0], arc2[0][1])], 'fixe', lw=0.6, dash=True)
text(ax, ax0 + 6, ay0 + 6, 'arc 0,1', 'varie', 's')
text(ax, ax0 + 6, ay0 - 6, 'hauteur 0,005', 'resultat', 's')
text(ax, 22, 3, 'presque tout droit', 'fixe', 's'); text(ax, 66, 3, 'presque à plat', 'fixe', 's')
save(fig, '30-012')
