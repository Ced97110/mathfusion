import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def sq(ax, cx, cy, s, ang, role):
    a = math.radians(ang); R = lambda px, py: (cx + s * (px * math.cos(a) - py * math.sin(a)), cy + s * (px * math.sin(a) + py * math.cos(a)))
    poly(ax, [R(-1, -1), R(1, -1), R(1, 1), R(-1, 1)], role)
    p = R(-.6, -.6); disc(ax, p[0], p[1], 1.2, "varie")
fig, ax = canvas(78)
text(ax, 44, 74, 'inversible : on défait', 'resultat', 's')
for x, a, l in [(14, 0, 'départ'), (44, 90, r'$u=r$'), (74, 0, r'$v$ : 3 quarts')]:
    sq(ax, x, 56, 6, a, 'sujet'); text(ax, x, 44, l, 'sujet', 's')
arrow(ax, (22, 56), (36, 56), 'varie'); arrow(ax, (52, 56), (66, 56), 'varie')
text(ax, 74, 66, r'$uv=1$', 'resultat', 's')
text(ax, 44, 34, r'pas inversible : $+2$ dans ℕ', 'limite', 's')
f = numberline(ax, 12, 76, 10, -2, 4, 1, arrow_right=False, role='fixe')
arrow(ax, (f(0), 14), (f(-2), 14), 'limite', curve=0.5)
text(ax, f(-1), 25, r'défaire : $-2$ ?', 'limite', 's')
save(fig, '44-094')
