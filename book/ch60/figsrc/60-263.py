import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(70)
cx, cy, R = 22, 40, 15
P = [(cx + R * math.cos(math.radians(90 + 72 * k)), cy + R * math.sin(math.radians(90 + 72 * k))) for k in range(5)]
poly(ax, P, 'sujet', lw=1.0)
for k in range(5):
    (x1, y1), (x2, y2) = P[k], P[(k + 1) % 5]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    nx, ny = (y2 - y1), -(x2 - x1); n = math.hypot(nx, ny); nx, ny = nx / n, ny / n
    line(ax, [(mx - nx * 1.2, my - ny * 1.2), (mx + nx * 1.2, my + ny * 1.2)], 'sujet', lw=0.9)
text(ax, 22, 17, 'polygone régulier', 'sujet', 's')
text(ax, 22, 10, 'constructible à la règle', 'varie', 's')
text(ax, 22, 4, 'et au compas ?', 'varie', 's')
arrow(ax, (39, 43), (49, 50), 'varie')
text(ax, 56, 63, 'ch. 66 : on étudie le groupe', 'varie', 's')
box(ax, 50, 46, 34, 12, 'autre', label=r'$(\mathbb{Z}/n)^{\times}$')
text(ax, 67, 41.5, 'groupe abélien fini', 'autre', 's')
arrow(ax, (67, 37), (67, 27), 'varie')
text(ax, 64, 32, 'théorème de structure', 'varie', 's', ha='right')
box(ax, 48, 14, 38, 12, 'resultat', label='somme de groupes cycliques', size='s')
save(fig, '60-263')
