import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
cx, cy, Rr, r = 44, 46, 24, 2.4

def edge(p, q, d):
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy)
    return (p[0] + dx / n * d, p[1] + dy / n * d)

ax.add_patch(Circle((cx, cy), Rr, ec=COL['fixe'], fc='none', lw=0.6, zorder=1))
pts = [(cx + Rr * math.cos(math.radians(72 * k)), cy + Rr * math.sin(math.radians(72 * k))) for k in range(5)]
# flèches ×z : de chaque point au suivant, en suivant le cercle
for k in range(5):
    p, q = pts[k], pts[(k + 1) % 5]
    arrow(ax, edge(p, q, r), edge(q, p, r), 'varie', curve=0.325)
for k, p in enumerate(pts):
    disc(ax, p[0], p[1], r, 'sujet')
    a = math.radians(72 * k)
    text(ax, cx + (Rr + 8) * math.cos(a), cy + (Rr + 6.5) * math.sin(a), f'{72 * k}°', 'sujet', 'm')
text(ax, cx, cy + 2.5, r'$z^5=1$', 'sujet', 'l')
text(ax, cx, cy - 3, r'$\times z$ : 72°', 'varie', 's')
text(ax, 44, 5, '5 × 72° = 360° : un tour complet', 'encre', 's')
save(fig, '64-147')
