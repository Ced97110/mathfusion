import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cx, cy, R = 44, 44, 28
pos = lambda k: (cx + R * math.cos(math.radians(90 - 30 * k)), cy + R * math.sin(math.radians(90 - 30 * k)))
for k in range(12):
    x, y = pos(k)
    if k in (0, 4, 8):
        disc(ax, x, y, 3.6, 'sujet' if k else 'fixe', label=str(k), size='m')
    else:
        disc(ax, x, y, 1.1, 'fixe')
def hop(a, b, lab):
    (x1, y1), (x2, y2) = pos(a), pos(b)
    d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    arrow(ax, (x1 + ux * 4, y1 + uy * 4), (x2 - ux * 4, y2 - uy * 4), 'varie')
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    text(ax, cx + (mx - cx) * 0.62, cy + (my - cy) * 0.62, lab, 'varie', 's')
hop(0, 4, 'pas 1'); hop(4, 8, 'pas 2'); hop(8, 0, 'pas 3')
text(ax, cx, cy, r'$+4$ à chaque pas', 'varie', 's')
text(ax, 44, 79, 'horloge à 12 heures', 'fixe', 'm')
text(ax, 44, 5, "3 pas : 4 est d'ordre 3", 'resultat', 'm')
save(fig, '50-141')
