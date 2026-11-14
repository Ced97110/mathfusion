import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(62)
d = math.tan(math.radians(30))
for x0, tilt in [(4, 0), (48, 10)]:
    O = (x0 + 2, 48); N = (x0 + 36, 48 - 34 * d)
    line(ax, [O, (x0 + 40, 48)], 'fixe', dash=True)
    t = math.radians(tilt)
    line(ax, [(N[0] - 34 * math.cos(t), N[1] - 34 * math.sin(t)), (N[0] + 3 * math.cos(t), N[1] + 3 * math.sin(t))], 'fixe')
    line(ax, [O, N], 'sujet', lw=1.6)
    disc(ax, *O, 1.0, 'sujet'); disc(ax, *N, 1.0, 'sujet')
    arc(O, 12, -30, 0, 'resultat'); text(ax, x0 + 18, 44.5, '30°', 'resultat', 's')
    ang = 30 + tilt
    arc(N, 9, 180 - 30 + 0, 180 + tilt, 'resultat' if tilt == 0 else 'limite')
    text(ax, N[0] - 15, N[1] + 3.5 - (0 if tilt == 0 else 0), '%d°' % ang, 'resultat' if tilt == 0 else 'limite', 's')
text(ax, 22, 12, 'deux horizontales parallèles', 'resultat', 's') if False else None
text(ax, 22, 14, 'parallèles : 30° = 30°', 'resultat', 's'); text(ax, 66, 14, 'inclinée : 30° ≠ 40°', 'limite', 's')
text(ax, 22, 8, 'angles égaux', 'resultat', 's'); text(ax, 66, 8, 'angles différents', 'limite', 's')
text(ax, 22, 58, 'cas normal', 'resultat', 'm'); text(ax, 66, 58, 'sol incliné de 10°', 'limite', 'm')
save(fig, '26-109')
