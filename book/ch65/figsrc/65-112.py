import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(62)
cx, cy, R = 24, 28, 15
pts = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in (90, 210, 330)]
def seg(p, q, r=4.3):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
    return (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r)
for i in range(3):
    a, b = seg(pts[i], pts[(i + 1) % 3])
    arrow(ax, a, b, 'varie')
for i, p in enumerate(pts):
    disc(ax, p[0], p[1], 3.6, 'sujet', label=r'$y_%d$' % (i + 1), size='s')
text(ax, cx, cy, r'$\sigma$', 'varie', 'l')
text(ax, 67, 54, r'$A_3=\{1,\ \sigma,\ \sigma^2\}$', 'sujet', 's')
text(ax, 67, 42, "trois répétitions de " + r'$\sigma$' + "\nramènent à l’identité", 'encre', 's')
text(ax, 67, 29, 'marche de taille 3', 'varie', 's')
arrow(ax, (67, 25), (67, 18), 'varie')
box(ax, 49, 4, 38, 14, 'resultat', label=r'$K(\sqrt{d})$' + "\n+ racine cubique", size='s')
save(fig, '65-112')
