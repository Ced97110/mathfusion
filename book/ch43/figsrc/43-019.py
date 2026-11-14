import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 24, 32, 17
P = lambda n, r=R: (cx + r*math.sin(math.radians(30*n)), cy + r*math.cos(math.radians(30*n)))
for n in range(12):
    x, y = P(n); disc(ax, x, y, 1.8, 'sujet' if n == 3 else 'fixe')
text(ax, cx, cy, '12 points', 'fixe', 's')
px, py = P(3)
for lab, y in (('3', 46), ('15', 36), ('−9', 26)):
    arrow(ax, (px+2.2, py), (53, y), 'fixe', lw=0.6)
    text(ax, 56, y, lab, 'sujet', 'm', ha='left')
text(ax, 56, 55, 'un point, trois noms', 'sujet', 's', ha='left')
box(ax, 50, 6, 36, 12, 'varie', label='autres noms : ±12')
save(fig, '43-019')
