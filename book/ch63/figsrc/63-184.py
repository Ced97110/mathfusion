import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# haut : trois racines de x^3 - 2 permutées par le groupe
cx, cy, R = 24, 58, 14
verts = [(cx + R * math.cos(math.radians(90 + 120 * k)), cy + R * math.sin(math.radians(90 + 120 * k))) for k in range(3)]
poly(ax, verts, 'fixe')
names = [r'$r$', r'$jr$', r'$j^2 r$']
offs = [(0, 4), (-5, -3), (6, -3)]
for (x, y), n, (dx, dy) in zip(verts, names, offs):
    disc(ax, x, y, 1.8, 'sujet'); text(ax, x + dx, y + dy, n, 'sujet', 's')
arrow(ax, (cx + 4, cy - 1), (cx - 4, cy - 1), 'varie', curve=-1.2)
text(ax, cx, cy - 7, 'permute', 'varie', 's') if False else None
text(ax, 62, 70, r'$G \subseteq S_n$', 'sujet', 'l')
text(ax, 62, 60, r'$n = 3$ : racines permutées', 'encre', 's')
text(ax, 62, 53, r'$G = S_3$ pour $x^3 - 2$', 'sujet', 's')
# bas : droite des degrés n
f = numberline(ax, 8, 70, 22, 3, 7, step=1, arrow_right=True, size='m')
ax.add_patch(Rectangle((f(5) - 1.5, 17.5), f(7) + 6 - f(5), 9, fc=FILL['limite'], ec=COL['limite'], lw=0.8, zorder=1))
text(ax, f(3), 29, r'$n = 3$', 'sujet', 's')
text(ax, (f(5) + f(7)) / 2 + 3, 30, r'$n \geq 5$ : $S_n$ non résoluble', 'limite', 's')
text(ax, 44, 7, r'$S_n$ : permutations des $n$ racines', 'fixe', 's')
save(fig, '63-184')
