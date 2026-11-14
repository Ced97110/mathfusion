import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(70)
cx, cy, R = 30, 36, 22
P = lambda k, r=R: (cx + r * math.sin(math.radians(24 * k)), cy + r * math.cos(math.radians(24 * k)))
for k in range(15):
    role = 'fixe'
    if k % 5 == 0 and k: role = 'sujet'
    if k % 3 == 0 and k: role = 'autre'
    if k == 8: role = 'resultat'
    if k == 0: role = 'encre'
    disc(ax, *P(k), 2.2, role if role != 'encre' else 'fixe', lw=0.8)
for k, r in [(0, 'encre'), (5, 'sujet'), (3, 'autre'), (8, 'resultat')]:
    text(ax, *P(k, R + 5.2), str(k), r, 's')
arrow(ax, P(0, R - 2.5), P(8, R - 2.5), 'resultat', curve=0.25)
arrow(ax, P(8, R - 2.5), P(1, R - 2.5), 'resultat', curve=0.25)
disc(ax, 60, 56, 2.0, 'sujet'); text(ax, 64, 56, r'$x=5$ : ordre 3', 'sujet', 's', ha='left')
disc(ax, 60, 46, 2.0, 'autre'); text(ax, 64, 46, r'$y=3$ : ordre 5', 'autre', 's', ha='left')
disc(ax, 60, 36, 2.0, 'resultat'); text(ax, 64, 36, r'$xy=8$', 'resultat', 's', ha='left')
text(ax, 64, 31, 'ordre 15', 'resultat', 's', ha='left')
text(ax, 66, 14, '15 sauts de 8', 'resultat', 's')
text(ax, 66, 9, 'pour revenir à 0', 'resultat', 's')
save(fig, '50-171')
