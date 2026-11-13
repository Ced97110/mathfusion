import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="fixe", lw=0.9, n=60):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw)
fig, ax = canvas(64)
r = 26.0; O = (29, 32)
cx, sy = 0.6, 0.8
arc(ax, O, r, 0, 360, 'resultat', 0.9, 120)
line(ax, [(O[0] - r - 2, O[1]), (O[0] + r + 2, O[1])], 'fixe', 0.6); line(ax, [(O[0], O[1] - r - 2), (O[0], O[1] + r + 2)], 'fixe', 0.6)
P = (O[0] + cx * r, O[1] + sy * r)
line(ax, [(P[0], O[1]), P], 'varie', 1.2); line(ax, [O, (P[0], O[1])], 'fixe', 1.2)
arrow(ax, O, P, 'sujet', lw=1.5)
text(ax, O[0] + cx * r / 2, O[1] - 3, '0,6', 'fixe', 's'); text(ax, P[0] + 4, O[1] + sy * r / 2, '0,8', 'varie', 's')
text(ax, O[0] + 4, O[1] + 20, 'longueur 1', 'resultat', 's', ha='left') if False else text(ax, O[0] - 3, O[1] + 18, 'longueur 1', 'sujet', 's')
text(ax, 72, 54, 'vecteur', 'sujet', 's'); text(ax, 72, 49, '(0,6 ; 0,8)', 'sujet', 's')
text(ax, 72, 40, 'nombre complexe', 'autre', 's'); text(ax, 72, 35, '0,6 + 0,8 $i$', 'autre', 's')
text(ax, 72, 24, 'mêmes deux nombres', 'fixe', 's'); text(ax, 72, 14, '0,36 + 0,64 = 1', 'resultat', 's')
text(ax, 72, 9, 'donc longueur 1', 'resultat', 's')
save(fig, '31-151')
