import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
cx, cy, R = 30, 36, 15
pos = lambda h, r=R: (cx + r * math.sin(math.radians(30 * h)), cy + r * math.cos(math.radians(30 * h)))
for h in range(12):
    role = {9: 'sujet', 4: 'resultat'}.get(h, 'fixe')
    disc(ax, *pos(h), 2.0 if role != 'fixe' else 1.3, role)
text(ax, *pos(12 if False else 0, R + 5), '12', 'fixe', 's')
text(ax, *pos(9, R + 5), '9', 'sujet', 'm', weight='bold')
text(ax, *pos(4, R + 5), '4', 'resultat', 'm', weight='bold')
arc = [pos(9 + 7 * t / 40, R + 8) for t in range(41)]
line(ax, arc[:-1], 'varie', lw=1.0)
arrow(ax, arc[-2], arc[-1], 'varie')
text(ax, *pos(1.5, R + 12.5), '+ 7', 'varie', 'm')
text(ax, 70, 62, r'$\bar{9}+\bar{7}=\bar{4}$', 'encre', 'l')
text(ax, 70, 48, 'on choisit 9 et 7', 'sujet', 's')
text(ax, 70, 38, r'$9+7=16$', 'varie', 'm')
text(ax, 70, 28, '16 est sur la', 'resultat', 's')
text(ax, 70, 22, 'position 4', 'resultat', 's')
save(fig, '43-123')
