import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 21, 56, r'$p = 2,\ q = 3$', 'encre', 'm')
text(ax, 21, 46, r'$3 \equiv 1 (\mathrm{mod}\ 2)$', 'resultat', 'm')
text(ax, 21, 36, r'$6 = 2 \times 3$', 'sujet', 'm')
text(ax, 21, 22, 'non commutatif', 'sujet', 'm')
cx, cy, R = 63, 36, 17
V = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in (90, 210, 330)]
poly(ax, V, 'sujet')
for i in range(3):
    p = V[i]; m = ((V[(i + 1) % 3][0] + V[(i + 2) % 3][0]) / 2, (V[(i + 1) % 3][1] + V[(i + 2) % 3][1]) / 2)
    dx, dy = m[0] - p[0], m[1] - p[1]; n = math.hypot(dx, dy); ux, uy = dx / n, dy / n
    line(ax, [(p[0] - 4 * ux, p[1] - 4 * uy), (m[0] + 4 * ux, m[1] + 4 * uy)], 'varie', lw=1.1, dash=True)
text(ax, 63, 61, r'$n_2 = 3$ axes', 'varie', 'm')
text(ax, 63, 7, 'chaque axe : 2 éléments', 'varie', 's')
save(fig, '50-178')
