import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def sq(cx, cy, s, role):
    pts = [(cx - s, cy - s), (cx + s, cy - s), (cx + s, cy + s), (cx - s, cy + s)]
    poly(ax, pts, 'fixe', fill=False)
    return pts
p1 = sq(22, 32, 11, 'sujet')
for p in p1: disc(ax, p[0], p[1], 2.2, 'sujet')
for k in range(4):
    a, b = p1[k], p1[(k + 1) % 4]
    arrow(ax, (a[0] + (b[0]-a[0])*0.2, a[1] + (b[1]-a[1])*0.2), (a[0] + (b[0]-a[0])*0.8, a[1] + (b[1]-a[1])*0.8), 'varie', curve=-0.0)
text(ax, 22, 54, 'Transitif', 'sujet', 'm', weight='bold'); text(ax, 22, 9, '1 orbite de 4 points', 'sujet', 's')
text(ax, 22, 3.5, 'tout est mélangé', 'varie', 's')
p2 = sq(66, 32, 11, 'fixe')
for p in p2: disc(ax, p[0], p[1], 2.2, 'fixe')
disc(ax, 66, 32, 2.8, 'autre')
text(ax, 66, 54, 'Point fixe', 'autre', 'm', weight='bold'); text(ax, 66, 9, 'orbite du centre : 1 point', 'autre', 's')
text(ax, 66, 3.5, 'le centre ne bouge pas', 'fixe', 's')
save(fig, '47-202')
