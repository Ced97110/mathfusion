import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def sq(cx, cy, s, role):
    h = s / 2; poly(ax, [(cx - h, cy - h), (cx + h, cy - h), (cx + h, cy + h), (cx - h, cy + h)], role)
def spin(cx, cy, R, deg, role):
    pts = [(cx + R * math.cos(math.radians(200 + d)), cy + R * math.sin(math.radians(200 + d))) for d in range(0, deg + 1, 5)]
    line(ax, pts[:-1], role, lw=1.2); arrow(ax, pts[-2], pts[-1], role, lw=1.2)
fig, ax = canvas(75)
line(ax, [(44, 6), (44, 70)], 'fixe', lw=0.6)
text(ax, 22, 70, 'carré : g = s, n = r', 'encre', 's')
sq(11, 46, 14, 'sujet'); spin(11, 46, 3.5, 90, 'sujet')
sq(34, 46, 14, 'resultat'); spin(34, 46, 3.5, 270, 'resultat')
arrow(ax, (19, 46), (26, 46), 'varie')
text(ax, 11, 34, 'n = r', 'sujet', 's')
text(ax, 34, 34, 'g⁻¹ n g = r³', 'resultat', 's')
text(ax, 22, 22, 'le conjugué n’est pas n', 'varie', 's')
text(ax, 66, 70, 'horloge : g = 2, n = 3', 'encre', 's')
f = lambda v: 50 + v * 6.4
y = 44
line(ax, [(f(0), y), (f(5), y)], 'fixe', lw=0.7)
for v in range(6): disc(ax, f(v), y, 0.6, 'fixe')
disc(ax, f(0), y, 1.6, 'fixe'); disc(ax, f(3), y, 1.9, 'resultat')
arrow(ax, (f(0), y + 1.5), (f(2), y + 1.5), 'varie', curve=-0.5); text(ax, f(1), y + 8, '+2', 'varie', 's')
arrow(ax, (f(2), y + 1.5), (f(5), y + 1.5), 'sujet', curve=-0.5); text(ax, f(3.5), y + 10, '+3', 'sujet', 's')
arrow(ax, (f(5), y - 1.5), (f(3), y - 1.5), 'varie', curve=-0.5); text(ax, f(4), y - 8, '−2', 'varie', 's')
text(ax, 66, 22, '−2 + 3 + 2 = 3 = n', 'resultat', 's')
save(fig, '47-124')
