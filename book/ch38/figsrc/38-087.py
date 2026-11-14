import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def secteur(ax, o, r, a0, a1, role):
    pts = [o] + [(o[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 40)), o[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 40))) for i in range(41)]
    poly(ax, pts, role)

fig, ax = canvas(64)
o = (44.0, 12.0)
R = 36.0
# trois angles mesurés posés l'un après l'autre à partir d'une droite (180°)
secteur(ax, o, R, 0, 62, 'sujet')
secteur(ax, o, R, 62, 120, 'autre')
secteur(ax, o, R, 120, 181, 'varie')
line(ax, [(o[0] - R - 2, o[1]), (o[0] + R + 2, o[1])], 'encre', lw=1.1)
for a in (62, 120, 181):
    line(ax, [o, (o[0] + R * math.cos(math.radians(a)), o[1] + R * math.sin(math.radians(a)))], 'encre', lw=0.8)
for a, lab, role in ((31, '62°', 'sujet'), (91, '58°', 'autre'), (150.5, '61°', 'varie')):
    text(ax, o[0] + 0.62 * R * math.cos(math.radians(a)), o[1] + 0.62 * R * math.sin(math.radians(a)), lab, role, 'm')
text(ax, 44, 58, '62° + 58° + 61° = 181°', 'encre', 'm')
text(ax, 76, 6, 'droite : 180°', 'encre', 's')
text(ax, 14, 6, '1° de trop', 'varie', 's')
save(fig, '38-087')
