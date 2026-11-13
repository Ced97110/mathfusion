import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

fig, ax = canvas(72)
text(ax, 44, 67, '3 défauts : les moyens sur place', 'limite', 's')
for cx, ttl in [(15, 'du soleil'), (44, 'un bâton'), (73, 'toute l’ombre')]:
    text(ax, cx, 61, 'il faut ' + ttl if ttl != 'toute l’ombre' else 'il faut toute l’ombre', 'encre', 's')
    line(ax, [(cx - 12, 32), (cx + 12, 32)], 'fixe', lw=0.8)
line(ax, [(10, 32), (10, 50)], 'varie', lw=1.8)
line(ax, [(10, 32), (24, 32)], 'limite', dash=True, lw=1.4)
text(ax, 15, 26, 'pas d’ombre', 'limite', 's')
line(ax, [(39, 32), (39, 50)], 'varie', lw=1.8); line(ax, [(39, 32), (50, 32)], 'sujet', lw=2.0)
line(ax, [(54, 32), (54, 39)], 'limite', dash=True, lw=1.2)
text(ax, 44, 26, 'pas de bâton', 'limite', 's')
box(ax, 72, 28, 13, 4, 'fixe')
line(ax, [(66, 32), (66, 50)], 'varie', lw=1.8); line(ax, [(66, 32), (76, 32)], 'sujet', lw=2.0)
line(ax, [(76, 32), (84, 32)], 'limite', dash=True, lw=1.2)
text(ax, 84, 36, '?', 'limite', 'm')
text(ax, 73, 22.5, 'ombre dans l’eau', 'limite', 's')
box(ax, 4, 3, 80, 13, 'resultat', label='le raisonnement reste vrai :\nrapport hauteur/ombre égal', size='s')
save(fig, '25-009')
