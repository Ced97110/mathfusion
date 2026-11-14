import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def cut(p, q, k):
    d = (q[0] - p[0], q[1] - p[1]); L = math.hypot(*d); u = (d[0] / L, d[1] / L)
    return (p[0] + u[0] * k, p[1] + u[1] * k), (q[0] - u[0] * k, q[1] - u[1] * k)
disc(ax, 13, 52, 5, 'resultat', label='000', size='s'); disc(ax, 13, 28, 5, 'resultat', label='111', size='s')
text(ax, 13, 66, 'fixes', 'resultat', 's')
for cx, labs, name in [(42, ['001', '100', '010'], 'tourne'), (71, ['011', '101', '110'], 'tourne')]:
    P = [(cx, cy) for cx, cy in [(cx, 52), (cx + 8, 33), (cx - 8, 33)]]
    for (px, py), l in zip(P, labs): disc(ax, px, py, 5, 'varie', label=l, size='s')
    for i in range(3):
        a, b = cut(P[i], P[(i + 1) % 3], 6.4)
        arrow(ax, a, b, 'varie', lw=1.0)
    text(ax, cx, 66, 'un cycle de 3', 'varie', 's')
text(ax, 44, 14, r'4 cycles : $2^{4}=16$ fonctions fixes', 'encre', 'm')
text(ax, 44, 76, r'le tour $a\to b\to c$', 'encre', 'm')
save(fig, '49-269')
