import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
a = 0.35
s = 34
ox, oy = 8, 16
arrow(ax, (3, oy), (86, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 3), (ox, oy + 34), 'fixe', lw=0.8)
pts = [(ox + s * a * (t - math.sin(t)), oy + s * a * (1 - math.cos(t))) for t in [2 * math.pi * i / 400 for i in range(401)]]
line(ax, pts, 'fixe', lw=1.0)
px, py = ox + s * a * math.pi, oy + s * a * 2
line(ax, [(px, oy), (px, py)], 'resultat', lw=1.0, dash=True)
line(ax, [(ox, py), (px, py)], 'resultat', lw=1.0, dash=True)
disc(ax, px, py, 1.5, 'sujet')
disc(ax, px, oy, 1.1, 'resultat')
disc(ax, ox, py, 1.1, 'resultat')
text(ax, px, oy - 4, 'f(t) = 1,10', 'resultat', 's')
text(ax, ox + 11, py + 4.2, 'g(t) = 0,70', 'resultat', 's')
text(ax, px, py + 5.5, '(x ; y) = (1,10 ; 0,70)', 'sujet', 'm')
arrow(ax, (ox + s * a * (0.9 - math.sin(0.9)) + 1, oy + s * a * (1 - math.cos(0.9))), (ox + s * a * (1.5 - math.sin(1.5)), oy + s * a * (1 - math.cos(1.5))), 'varie', lw=1.2, curve=-0.2)
text(ax, 31, 24, 't augmente', 'varie', 's')
save(fig, '40-091')
