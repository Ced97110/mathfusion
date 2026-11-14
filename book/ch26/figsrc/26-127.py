import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(72)
u = 20; s3 = math.sqrt(3)
# carré de côté 1 : sa moitié est un triangle rectangle
a = (6, 22); b = (a[0] + u, 22); c = (b[0], 22 + u); dd = (a[0], 22 + u)
poly(ax, [a, b, c], 'sujet'); line(ax, [a, dd, c], 'fixe', dash=True); sq(ax, b, (-1, 0), (0, 1))
text(ax, 16, 18.5, '1', 'sujet', 's'); text(ax, 29, 32, '1', 'sujet', 's'); text(ax, 11, 37, r'$\sqrt{2}$', 'sujet', 'l')
text(ax, 13, 25.5, '45°', 'varie', 's')
# triangle équilatéral de côté 2 : sa moitié est un triangle rectangle
v = 17
d = (66, 22); e = (66 + v, 22); f = (66, 22 + v * s3); g = (66 - v, 22)
poly(ax, [d, e, f], 'sujet'); line(ax, [d, g, f, d], 'fixe', dash=True); sq(ax, d, (1, 0), (0, 1))
text(ax, 74.5, 18.5, '1', 'sujet', 's'); text(ax, 62, 36, r'$\sqrt{3}$', 'sujet', 'm'); text(ax, 80, 42, '2', 'sujet', 'm')
text(ax, 77.5, 25.5, '60°', 'varie', 's'); text(ax, 69.5, 46, '30°', 'varie', 's')
text(ax, 44, 66, 'à la règle et au compas', 'fixe', 'm')
arrow(ax, (22, 63), (16, 44.5), 'fixe'); arrow(ax, (62, 63), (66, 57), 'fixe')
text(ax, 17, 11, r'$\sin 45°=\frac{\sqrt{2}}{2}$', 'resultat', 's')
text(ax, 64, 11, r'$\sin 30°=\frac{1}{2}$', 'resultat', 's'); text(ax, 64, 3.5, r'$\sin 60°=\frac{\sqrt{3}}{2}$', 'resultat', 's')
save(fig, '26-127')
