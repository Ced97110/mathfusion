import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(80)
r, cx, cy = 24, 44, 48
pts = arc(cx, cy, r, math.pi / 2 - 1, math.pi / 2 + 1)
Q, P = pts[0], pts[-1]
line(ax, pts, 'sujet', lw=1.8)
line(ax, [P, Q], 'autre', lw=1.8)
disc(ax, P[0], P[1], 0.9, 'encre'); disc(ax, Q[0], Q[1], 0.9, 'encre')
text(ax, P[0] - 3, P[1], r'$P$'); text(ax, Q[0] + 3, Q[1], r'$Q$')
text(ax, 44, cy + r + 4, 'arc : 6 cm', 'sujet')
text(ax, 44, P[1] - 4.5, 'corde : 5,05 cm', 'autre')
box(ax, 22, 36, 6 * 8, 5, 'sujet', label='6 cm', size='s')
box(ax, 22, 27, 5.05 * 8, 5, 'autre', label='5,05 cm', size='s')
text(ax, 20, 38.5, 'arc', 'sujet', 's', ha='right'); text(ax, 20, 29.5, 'corde', 'autre', 's', ha='right')
text(ax, 44, 16, r'$6 > 5{,}05$', 'resultat', 'l')
text(ax, 44, 9, 'l’arc est plus long', 'resultat', 'm')
save(fig, '29-096')
