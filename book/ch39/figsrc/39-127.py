import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
R = 17; Y = 42
cxs = (22, 66)
def pt(cx, k, r=R):
    a = math.radians(45 * k); return (cx + r * math.cos(a), Y + r * math.sin(a))
def chord(cx, a, b, role):
    p, q = pt(cx, a), pt(cx, b)
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + 2 * ux, p[1] + 2 * uy), (q[0] - 2 * ux, q[1] - 2 * uy), role, lw=0.9)
for cx in cxs:
    ax.add_patch(Circle((cx, Y), R, ec=COL['fixe'], fc='none', lw=0.5, zorder=1, ls='--'))
visited = [0, 2, 4, 6]
for i in range(4): chord(cxs[0], visited[i], visited[(i + 1) % 4], 'varie')
for k in range(8):
    disc(ax, *pt(cxs[0], k), 1.5, 'varie' if k in visited else 'fixe')
seq = [(3 * j) % 8 for j in range(9)]
for a, b in zip(seq, seq[1:]): chord(cxs[1], a, b, 'resultat')
for k in range(8): disc(ax, *pt(cxs[1], k), 1.5, 'resultat')
text(ax, cxs[0], 68, r'$\omega^2=i$ : pas de $90^\circ$', 'varie', 's')
text(ax, cxs[1], 68, r'$\omega^3$ : pas de $135^\circ$', 'resultat', 's')
text(ax, cxs[0], 14, '4 points', 'varie', 'l')
text(ax, cxs[1], 14, '8 points', 'resultat', 'l')
text(ax, cxs[0], 7, 'pas primitive', 'varie', 's')
text(ax, cxs[1], 7, 'primitive', 'resultat', 's')
text(ax, cxs[1], 21, r'$135^\circ,\,270^\circ,\,45^\circ\dots$', 'resultat', 's')
save(fig, '39-127')
