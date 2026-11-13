import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 61, r'$n_p = 1$', 'resultat', 'l', weight='bold')
text(ax, 66, 61, r'$n_p > 1$', 'limite', 'l', weight='bold')
text(ax, 22, 55, 'groupe de 15 éléments', 'fixe', 's')
text(ax, 66, 55, '6 symétries du triangle', 'fixe', 's')
box(ax, 4, 32, 36, 18, 'sujet'); text(ax, 22, 46, r'$n_3 = 1$', 'sujet', 's')
for i in range(3): disc(ax, 22 + (i - 1) * 6, 36, 1.6, 'sujet')
box(ax, 4, 9, 36, 18, 'sujet'); text(ax, 22, 23, r'$n_5 = 1$', 'sujet', 's')
for i in range(5): disc(ax, 22 + (i - 2) * 6, 13, 1.6, 'sujet')
text(ax, 22, 3.5, 'un seul : normal', 'resultat', 's')
cx, cy, R = 66, 36, 12
V = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in (90, 210, 330)]
poly(ax, V, 'fixe')
for i in range(3):
    v = V[i]; m = ((V[(i + 1) % 3][0] + V[(i + 2) % 3][0]) / 2, (V[(i + 1) % 3][1] + V[(i + 2) % 3][1]) / 2)
    dx, dy = v[0] - m[0], v[1] - m[1]; n = math.hypot(dx, dy)
    line(ax, [m, (v[0] + dx / n * 3, v[1] + dy / n * 3)], 'varie', lw=1.2)
text(ax, 66, 16, r'$n_2 = 3$, 2 éléments chacun', 'varie', 's')
text(ax, 66, 3.5, 'aucun n’est normal', 'limite', 's')
save(fig, '50-241')
