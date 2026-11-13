import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
ox, oy, R = 10, 7, 40
line(ax, [(ox - 3, oy), (ox + R + 6, oy)], 'fixe'); line(ax, [(ox, oy - 3), (ox, oy + R + 6)], 'fixe')
th = [math.radians(a * 90 / 40) for a in range(41)]
line(ax, [(ox + R * math.cos(t), oy + R * math.sin(t)) for t in th], 'fixe')
a = math.radians(15); P = (ox + R * math.cos(a), oy + R * math.sin(a))
poly(ax, [(ox, oy), (ox + R, oy), (ox + R, oy + R)] if False else [(ox, oy), (P[0], oy), P], 'resultat')
line(ax, [(ox, oy), P], 'sujet', lw=1.4)
arrow(ax, (ox + 1, oy - 2.2), (P[0] - 1, oy - 2.2), 'resultat')
text(ax, P[0] / 2 + 5, oy - 5.5, '0,9659 vers la droite', 'resultat', 's')
line(ax, [(P[0], oy), P], 'fixe', lw=1.0)
text(ax, P[0] + 2, oy + 5.2, '0,2588', 'fixe', 's', ha='left')
text(ax, ox + 25, oy + 2.0, '15°', 'varie', 's')
text(ax, ox + 16, oy + 22, '1er quadrant', 'fixe', 's')
text(ax, ox + 16, oy + 40, 'cosinus positif', 'resultat', 's')
save(fig, '34-133')
