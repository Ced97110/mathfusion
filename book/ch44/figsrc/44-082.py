import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def sq(ax, cx, cy, s, ang, role):
    a = math.radians(ang); R = lambda px, py: (cx + s * (px * math.cos(a) - py * math.sin(a)), cy + s * (px * math.sin(a) + py * math.cos(a)))
    poly(ax, [R(-1, -1), R(1, -1), R(1, 1), R(-1, 1)], role)
    p = R(-.6, -.6); disc(ax, p[0], p[1], 1.5, 'varie')
fig, ax = canvas(58)
xs = [12, 33, 54, 75]
for i, (x, l) in enumerate(zip(xs, [r'$1$', r'$r$', r'$r^{2}$', r'$r^{3}$'])):
    sq(ax, x, 34, 6.5, 90 * i, 'sujet')
    text(ax, x, 22, l, 'sujet', 'm')
    text(ax, x, 47, f'{i} fois', 'fixe', 's')
arrow(ax, (75, 18), (12, 18), 'resultat', curve=-0.25)
text(ax, 44, 4, r'$r^{4}=1$ : on revient', 'resultat', 'm')
save(fig, '44-082')
