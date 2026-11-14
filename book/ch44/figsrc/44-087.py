import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def sq(ax, cx, cy, s, ang, role):
    a = math.radians(ang); R = lambda px, py: (cx + s * (px * math.cos(a) - py * math.sin(a)), cy + s * (px * math.sin(a) + py * math.cos(a)))
    poly(ax, [R(-1, -1), R(1, -1), R(1, 1), R(-1, 1)], role)
    p = R(-.6, -.6); disc(ax, p[0], p[1], 1.2, "varie")
fig, ax = canvas(66)
box(ax, 2, 4, 84, 58, 'fixe')
text(ax, 44, 56, r'$M(S)$ : toutes les transformations', 'fixe', 's')
box(ax, 8, 8, 72, 40, 'sujet', fill=True)
for i, (x, l) in enumerate(zip([20, 38, 56, 74], [r'$1$', r'$r$', r'$r^{2}$', r'$r^{3}$'])):
    pass
xs = [20, 36, 52, 68]
for i, (x, l) in enumerate(zip(xs, [r'$1$', r'$r$', r'$r^{2}$', r'$r^{3}$'])):
    sq(ax, x, 33, 5.5, 90 * i, 'sujet')
    text(ax, x, 22, l, 'sujet', 'm')
text(ax, 44, 13, 'contient 1 ; reste stable', 'sujet', 's')
save(fig, '44-087')
