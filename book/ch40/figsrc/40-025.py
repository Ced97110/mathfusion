import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(60)
c = (8.0, 12.0); L = 38.0
pp = lambda r, t: (c[0] + r * cos(t), c[1] + r * sin(t))
T = lambda a, b, n: [a + (b - a) * i / n for i in range(n + 1)]
arrow(ax, c, (c[0] + L + 6, c[1]), 'fixe', lw=1.2)
text(ax, c[0] + 30, c[1] - 5, 'axe polaire : départ', 'fixe', 's')
t = radians(60)
arrow(ax, c, pp(L, t), 'sujet', lw=1.2)
line(ax, [pp(14, a) for a in T(0, t, 30)], 'varie', lw=1.3)
arrow(ax, pp(14, t - 0.05), pp(14, t + 0.12), 'varie', lw=1.3)
text(ax, c[0] + 19, c[1] + 6, r'$\theta$', 'varie', 'xl')
disc(ax, *c, 1.2, 'encre')
text(ax, c[0] - 2, c[1] - 4.5, '$O$', 'encre', 's')
text(ax, 62, 50, 'sens inverse\ndes aiguilles', 'varie', 's')
text(ax, 62, 36, '$\\theta=\\pi/3$ (60°)\nune valeur choisie', 'sujet', 's')
box(ax, 54, 4, 32, 9, 'resultat', label='$r=1+\\cos\\theta$', size='s')
save(fig, '40-025')
