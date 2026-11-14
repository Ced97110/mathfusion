import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
c = (44, 44)
u = 14
P = (c[0] + u, c[1] - u)
line(ax, [(6, 44), (82, 44)], 'fixe', lw=0.6)
line(ax, [(44, 22), (44, 68)], 'fixe', lw=0.6)
line(ax, [c, P], 'fixe', lw=1.0)
def arc(r, a0, a1, role):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * j / 60)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * j / 60))) for j in range(61)]
    line(ax, pts, role, lw=1.2)
    arrow(ax, pts[-3], pts[-1], role, lw=1.2)
arc(8, 0, -45, 'sujet')
arc(17, 0, 315, 'resultat')
disc(ax, *P, 1.5, 'fixe')
text(ax, 53, 48.5, '−45°', 'sujet', 's')
text(ax, 25, 53, '315°', 'resultat', 's')
text(ax, 66, 34, r'$(1,\ -1)$', 'fixe', 's')
text(ax, 44, 18, r'$\arctan(-1) = -45°$', 'sujet', 'm')
text(ax, 44, 11, '−45° + 360° = 315°', 'resultat', 'm')
text(ax, 44, 4, 'même direction du point', 'encre', 's')
save(fig, '39-036')
