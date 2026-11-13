import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(66)
cx, cy, R, r = 22, 38, 12, 5
pts = []
for k in range(10):
    rad = R if k % 2 == 0 else r
    a = math.radians(90 + 36*k)
    pts.append((cx + rad*math.cos(a), cy + rad*math.sin(a)))
poly(ax, pts, 'autre')
text(ax, cx, 21, 'étoile à 5 bras', 'autre', 's')
text(ax, cx, 17.5, 'ordre 5 : oui', 'autre', 's')
gx, gy, s = 52, 28, 7
for i in range(4):
    for j in range(4):
        box(ax, gx + i*s, gy + j*s, s, s, 'sujet', r=0.2, lw=0.6)
text(ax, gx + 2*s, 21, 'grille de carrés', 'sujet', 's')
text(ax, gx + 2*s, 17.5, 'ordre 4 : oui', 'sujet', 's')
box(ax, 4, 4, 80, 7.5, 'resultat', label='dessin qui se répète : 1, 2, 3, 4, 6', size='s')
text(ax, 44, 64, 'un dessin qui se répète : jamais 5, ni 7', 'limite', 's')
save(fig, '74-086')
