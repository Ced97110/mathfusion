import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="fixe", lw=0.9, n=60):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw)
fig, ax = canvas(52)
u = 24.0; O = (18, 6)
c, s = math.cos(math.radians(30)), 0.5
rot = lambda x, y: (O[0] + (x * c - y * s) * u, O[1] + (x * s + y * c) * u)
poly(ax, [rot(0, 0), rot(1, 0), rot(1, 1), rot(0, 1)], 'resultat')
poly(ax, [O, (O[0] + u, O[1]), (O[0] + u, O[1] + u), (O[0], O[1] + u)], 'sujet')
poly(ax, [rot(0, 0), rot(1, 0), rot(1, 1), rot(0, 1)], 'resultat', fill=False, lw=1.2)
arc(ax, O, 14, 0, 30, 'varie', 1.1)
text(ax, O[0] + 17.5, O[1] + 3, r'$30°$', 'varie', 's')
text(ax, 12, 8.5 + 2 * 0, 'aire 1', 'sujet', 's') if False else None
text(ax, O[0] + 12, O[1] - 3, 'aire 1', 'sujet', 's')
text(ax, rot(0.5, 1.12)[0] - 4, rot(0.5, 1.12)[1] + 3, 'aire 1', 'resultat', 's')
text(ax, 66, 44, 'matrice de rotation', 'fixe', 's')
text(ax, 62, 36, '0,866', 'fixe', 's'); text(ax, 77, 36, '−0,5', 'fixe', 's')
text(ax, 62, 30, '0,5', 'fixe', 's'); text(ax, 77, 30, '0,866', 'fixe', 's')
line(ax, [(55.5, 27), (54.5, 27), (54.5, 39), (55.5, 39)], 'fixe'); line(ax, [(83.5, 27), (84.5, 27), (84.5, 39), (83.5, 39)], 'fixe')
text(ax, 66, 21, r'déterminant', 'varie', 's'); text(ax, 66, 16, '0,75 + 0,25 = 1', 'resultat', 's')
text(ax, 66, 8, r'$\cos^2\theta + \sin^2\theta = 1$', 'resultat', 's')
save(fig, '31-153')
