import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(84)
text(ax, 30, 80, 'Départ : trois dangers', 'encre', 'm', weight='bold')
# colonne 1
arrow(ax, (26, 66), (4, 66), 'limite', lw=0.9)
for x in range(8, 25, 4): line(ax, [(x, 64.8), (x, 67.2)], 'limite', lw=0.8)
# colonne 2 : boucle horaire
C = [(44, 72), (50, 66), (44, 60), (38, 66)]
for x, y in C: disc(ax, x, y, 1.3, 'limite')
for i in range(4):
    p, q = C[i], C[(i+1) % 4]; dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    arrow(ax, (p[0]+ux*1.6, p[1]+uy*1.6), (q[0]-ux*1.6, q[1]-uy*1.6), 'limite', lw=0.9, curve=-0.3)
# colonne 3
line(ax, [(62, 66), (84, 66)], 'fixe')
for x in (62, 67, 72): disc(ax, x, 66, 1.3, 'sujet')
arrow(ax, (63.2, 66.6), (65.8, 66.6), 'varie', lw=0.9, curve=-0.9)
arrow(ax, (68.2, 66.6), (70.8, 66.6), 'varie', lw=0.9, curve=-0.9)
disc(ax, 82, 66, 1.3, 'limite')
# aucun chemin n'atteint le point isolé : flèche pointillée barrée
arrow(ax, (73.4, 67.4), (80.6, 67.4), 'limite', lw=0.8, curve=-0.5)
ax.patches[-1].set_linestyle('--')
line(ax, [(75.8, 69.0), (78.2, 72.6)], 'limite', lw=1.2); line(ax, [(75.8, 72.6), (78.2, 69.0)], 'limite', lw=1.2)
for x, s in ((15, 'sans début'), (44, 'boucle'), (73, 'en trop')): text(ax, x, 55, s, 'limite', 's')
box(ax, 4, 41, 22, 8, 'sujet', label='axiome 1')
box(ax, 33, 41, 22, 8, 'sujet', label='axiome 2')
box(ax, 62, 41, 22, 8, 'sujet', label='axiome 3', weight='bold', lw=1.6)
box(ax, 59, 37, 27, 37, 'varie', fill=False, dash=True, lw=1.4)
text(ax, 73, 78, 'étape difficile', 'varie', 's', weight='bold')
for p, q, w in (((15, 41), (16, 20), 0.9), ((44, 41), (36, 20), 0.9), ((73, 37), (54, 20), 2.2)): arrow(ax, p, q, 'resultat', lw=w)
f = numberline(ax, 12, 60, 16, 0, 3, role='resultat')
disc(ax, 12, 16, 1.5, 'resultat'); ax.patches[-1].set_zorder(3.5)
text(ax, 75, 16, 'Arrivée : ℕ', 'resultat', 'm', weight='bold')
save(fig, '01-040')
