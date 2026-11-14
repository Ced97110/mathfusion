import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'$[K:\mathbb{Q}]=[K:\mathbb{Q}(r_1)]\times5$', 'sujet', 'm')
box(ax, 3, 52, 24, 11, 'sujet', label='$K$')
box(ax, 3, 30, 24, 11, 'sujet', label=r'$\mathbb{Q}(r_1)$')
box(ax, 3, 8, 24, 11, 'sujet', label=r'$\mathbb{Q}$')
arrow(ax, (15, 42), (15, 51), 'varie'); arrow(ax, (15, 20), (15, 29), 'varie')
text(ax, 18, 46.5, r'$[K:\mathbb{Q}(r_1)]$', 'varie', 's', ha='left'); text(ax, 18, 24.5, '5', 'varie', 'm', ha='left')
cx, cy, R = 65, 42, 11
V = [(cx + R * math.cos(math.radians(90 - 72 * k)), cy + R * math.sin(math.radians(90 - 72 * k))) for k in range(5)]
for k in range(5):
    a, b = V[k], V[(k + 1) % 5]
    d = math.hypot(b[0] - a[0], b[1] - a[1]); ux, uy = (b[0] - a[0]) / d, (b[1] - a[1]) / d
    arrow(ax, (a[0] + 2.6 * ux, a[1] + 2.6 * uy), (b[0] - 2.6 * ux, b[1] - 2.6 * uy), 'resultat')
for k, (x, y) in enumerate(V):
    disc(ax, x, y, 2.2, 'sujet')
    a = math.radians(90 - 72 * k)
    text(ax, cx + (R + 7) * math.cos(a), cy + (R + 6) * math.sin(a), f'$r_{k + 1}$', 'sujet', 's')
text(ax, 65, 20, '5-cycle : d’ordre 5', 'resultat', 'm')
text(ax, 65, 12, r'Cauchy : 5 divise $|G|$', 'resultat', 's')
save(fig, '64-180')
