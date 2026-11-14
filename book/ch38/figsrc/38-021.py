import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(60)
line(ax, [(44, 6), (44, 56)], 'fixe', lw=0.6, dash=True)
# ruban : mesure une longueur en la parcourant
text(ax, 22, 54, 'ruban', 'autre', 'l')
y = 32
line(ax, [(5, y), (39, y)], 'autre', lw=2.0)
for i in range(8):
    x = 5 + i * 34 / 7
    line(ax, [(x, y - 1.4), (x, y + 1.4)], 'autre', lw=0.8)
text(ax, 22, 22, 'mesure une longueur', 'autre', 's')
text(ax, 22, 15, 'on le pose le long', 'autre', 's')
# théodolite : trépied, lunette, cercle gradué
text(ax, 66, 54, 'théodolite', 'sujet', 'l')
apex = (66, 26)
for lx in (56, 66, 76):
    line(ax, [apex, (lx, 8)], 'sujet', lw=1.2)
box(ax, 61, 26, 10, 6, 'sujet')
pv = (66, 29)
tip = (pv[0] + 17, pv[1] + 17 * math.tan(math.radians(18)))
line(ax, [pv, tip], 'sujet', lw=2.4)
disc(ax, 66, 42, 5.5, 'sujet')
for k in range(12):
    a = math.radians(30 * k)
    line(ax, [(66 + 4.4 * math.cos(a), 42 + 4.4 * math.sin(a)), (66 + 5.5 * math.cos(a), 42 + 5.5 * math.sin(a))], 'sujet', lw=0.6)
text(ax, 66, 42, '18°', 'varie', 's', weight='bold')
text(ax, 66, 3, 'on lit des degrés', 'sujet', 's')
save(fig, '38-021')
