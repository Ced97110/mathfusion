import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
V = {'A': (12, 52), 'B': (12, 24), 'C': (40, 24), 'D': (40, 52)}
poly(ax, list(V.values()), 'fixe', fill=False)
(ax1, ay1), (ax2, ay2) = V['A'], V['C']
line(ax, [(ax1 - 4, ay1 + 4), (ax2 + 4, ay2 - 4)], 'fixe', lw=1.0, dash=True)
order = ['A', 'B', 'C', 'D']
for i, n in enumerate(order):
    p, q = V[n], V[order[(i + 1) % 4]]
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + 4.4 * ux, p[1] + 4.4 * uy), (q[0] - 4.4 * ux, q[1] - 4.4 * uy), 'varie', curve=0.25)
for n, (x, y) in V.items():
    disc(ax, x, y, 3.4, 'sujet', fill=(n == 'A'), label=n, size='m')
text(ax, 52, 50, 'orbite : les 4 sommets', 'varie', 's', ha='left')
text(ax, 52, 44, 'par le quart de tour', 'varie', 's', ha='left')
text(ax, 52, 30, 'axe AC : A et C restent', 'fixe', 's', ha='left')
text(ax, 52, 24, 'en place (stabilisateur)', 'fixe', 's', ha='left')
text(ax, 26, 8, 'A : en bleu plein', 'sujet', 's')
save(fig, '49-112')
