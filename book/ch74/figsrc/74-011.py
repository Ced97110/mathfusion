import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def star(cx, cy, R, r, role, rot=90):
    pts = []
    for i in range(10):
        a = math.radians(rot + i * 36); rr = R if i % 2 == 0 else r
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    poly(ax, pts, role)
fig, ax = canvas(60)
for a in range(3):
    for b in range(3):
        box(ax, 3 + a * 15, 6 + b * 15, 15, 15, 'sujet')
text(ax, 25.5, 56, 'carreaux carrés', 'sujet', 'm')
text(ax, 25.5, 2.8, 'se posent sans trou', 'resultat', 's')
text(ax, 54, 28.5, '+', 'encre', 'xl', weight='bold')
box(ax, 62, 19.5, 18, 18, 'fixe', fill=False, dash=True)
star(71, 28.5, 7.4, 3.1, 'varie')
text(ax, 71, 56, 'dessin', 'varie', 'm')
text(ax, 71, 14, 'cinq branches', 'varie', 's')
save(fig, '74-011')
