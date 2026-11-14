import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(84)
cx, cy, R = 36, 42, 22
ang = [0, 120, 240]
pts = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in ang]
poly(ax, pts, 'sujet')
# les trois axes de réflexion : droite par le centre et un sommet
for a in ang:
    ux, uy = math.cos(math.radians(a)), math.sin(math.radians(a))
    line(ax, [(cx - (0.5 * R + 9) * ux, cy - (0.5 * R + 9) * uy), (cx + (R - 3.5) * ux, cy + (R - 3.5) * uy)], 'varie', dash=True, lw=0.8)
for k, (x, y) in enumerate(pts):
    disc(ax, x, y, 3.4, 'sujet', label=f'$r_{k + 1}$', size='s')
# l'échange de r2 et r3 par pliage sur l'axe horizontal
arrow(ax, (pts[1][0] + 5, pts[1][1] - 4), (pts[2][0] + 5, pts[2][1] + 4), 'resultat', both=True)
text(ax, 78, 54, 'un axe\npar sommet', 'varie', 's')
text(ax, 77, 28, '$r_2$ et $r_3$\néchangés,\n$r_1$ ne bouge pas', 'resultat', 's')
text(ax, 44, 4, '3 réflexions : 3 échanges', 'varie', 's')
save(fig, '65-015')
