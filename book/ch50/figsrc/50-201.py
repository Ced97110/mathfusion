import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def shrink(p, q, d):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / L, (q[1] - p[1]) / L)
    return (p[0] + u[0] * d, p[1] + u[1] * d), (q[0] - u[0] * d, q[1] - u[1] * d)
text(ax, 22, 63, r'ℤ/$p^2$ℤ', 'sujet', 'l', weight='bold'); text(ax, 66, 63, r'ℤ/$p$ℤ × ℤ/$p$ℤ', 'autre', 'l', weight='bold')
pts = [(22 + 12 * math.cos(math.radians(90 - 40 * i)), 38 + 12 * math.sin(math.radians(90 - 40 * i))) for i in range(9)]
for i in range(9):
    p, q = shrink(pts[i], pts[(i + 1) % 9], 2.2); arrow(ax, p, q, 'sujet', lw=0.9)
for i, (x, y) in enumerate(pts): disc(ax, x, y, 1.6, 'fixe' if i == 0 else 'sujet')
text(ax, 22, 54.5, r'$e$', 'encre', 's')
g = [(57 + 9 * i, 29 + 9 * j) for j in range(3) for i in range(3)]; assert len(g) == 9
for k, (x, y) in enumerate(g): disc(ax, x, y, 1.8, 'fixe' if k == 0 else 'autre')
text(ax, 52.5, 29, r'$e$', 'encre', 's')
arrow(ax, (59, 29), (64, 29), 'varie'); arrow(ax, (68, 29), (73, 29), 'varie'); arrow(ax, (75, 27.3), (57, 27.3), 'varie', curve=-0.5)
text(ax, 22, 14, 'un élément d’ordre 9', 'sujet', 's'); text(ax, 66, 14, 'tous les autres : ordre 3', 'autre', 's')
text(ax, 44, 6, r'exemple $p=3$ : 9 éléments', 'fixe', 's')
save(fig, '50-201')
