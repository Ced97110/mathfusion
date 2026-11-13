import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
GL = {
 'F': [[(-.35,-.5),(-.35,.5),(.4,.5)], [(-.35,.05),(.2,.05)]],
 'V': [[(-.5,.5),(0,-.5),(.5,.5)]],
 'D': [[(-.4,-.5),(-.4,.5),(0,.5),(.25,.4),(.4,.2),(.45,0),(.4,-.2),(.25,-.4),(0,-.5),(-.4,-.5)]],
 'N': [[(-.4,-.5),(-.4,.5),(.4,-.5),(.4,.5)]],
}
def gd(ax, k, cx, cy, s, role='sujet', fx=1, fy=1, ang=0, lw=1.2):
    c, sn = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    for st in GL[k]:
        pts = []
        for x, y in st:
            x, y = x * fx * s, y * fy * s
            pts.append((cx + x * c - y * sn, cy + x * sn + y * c))
        line(ax, pts, role, lw=lw)
def dline(ax, p, q, role='varie', lw=0.9):
    line(ax, [p, q], role, lw=lw, dash=True)
fig, ax = canvas(98)
sx = 14 + 7 * 5 + 2.7
text(ax, 50, 94, 'les dix groupes ponctuels', 'sujet', 's')
for i in range(10):
    box(ax, 14 + 7 * i, 80, 5.4, 5.4, 'sujet' if i == 5 else 'fixe', r=0.4)
text(ax, 2, 83, 'niveau 1', 'encre', 's', ha='left')
text(ax, sx - 4, 74.5, 'un seul miroir', 'sujet', 's', ha='right')
arrow(ax, (sx, 79.5), (sx, 64.5), 'varie')
text(ax, 2, 58, 'niveau 2', 'encre', 's', ha='left')
box(ax, sx - 19, 52, 38, 12, 'fixe', label='type de réseau compatible', size='s')
text(ax, 2, 32, 'niveau 3', 'encre', 's', ha='left')
for x, t in [(14, 'vrai miroir'), (38, 'symétrie glissée'), (62, 'les deux')]:
    box(ax, x, 26, 22, 12, 'resultat', label=t, size='s')
    arrow(ax, (sx, 51.5), (x + 11, 38.8), 'varie')
brace(ax, 14, 84, 24, 'resultat', '3 papiers')
arrow(ax, (sx + 4, 87.5), (14 + 7 * 9 + 2.7, 87.5), 'varie')
text(ax, 62, 90.5, 'puis le groupe suivant', 'varie', 's')
text(ax, 44, 8, 'à la fin : 17 groupes', 'resultat', 'm')
save(fig, '74-152')
