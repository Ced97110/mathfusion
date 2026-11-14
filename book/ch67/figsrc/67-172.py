import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
cx, cy, R, r = 44, 46, 26, 3.2
def pos(k, rad=R):
    t = math.radians(90 - 24 * k)
    return cx + rad * math.cos(t), cy + rad * math.sin(t)
for k in range(15):
    x, y = pos(k)
    disc(ax, x, y, r, 'resultat' if k == 0 else 'sujet')
for k in range(15):
    (x0, y0), (x1, y1) = pos(k), pos((k + 1) % 15)
    d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
    arrow(ax, (x0 + ux * (r + 0.4), y0 + uy * (r + 0.4)), (x1 - ux * (r + 0.4), y1 - uy * (r + 0.4)), 'varie')
for k, s in [(0, r'$\alpha^0=1$'), (1, r'$\alpha^1$'), (2, r'$\alpha^2$'), (14, r'$\alpha^{14}$')]:
    x, y = pos(k, R + 8)
    text(ax, x, y, s, 'fixe', 's')
text(ax, 44, 48, r'$\alpha^{15}=1$', 'resultat')
text(ax, 44, 41, r'comme $k$ modulo 15', 'fixe', 's')
text(ax, 44, 7, '15 éléments, chacun une fois', 'resultat')
save(fig, '67-172')
