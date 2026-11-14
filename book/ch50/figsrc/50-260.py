import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 22, 68, r'6 : $\mathbb{Z}/3$ et ordre 2', 'encre', 's', weight='bold')
text(ax, 66, 68, r'21 : $\mathbb{Z}/7$ et ordre 3', 'encre', 's', weight='bold')
def pts(cx, cy, R, n, a0=90): return [(cx + R * math.cos(math.radians(a0 - 360 * k / n)), cy + R * math.sin(math.radians(a0 - 360 * k / n))) for k in range(n)]
def sh(p, q, d):
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy); return (p[0] + dx / n * d, p[1] + dy / n * d)
L = pts(22, 44, 9, 3)
for i, r in enumerate(['sujet', 'varie', 'varie']): disc(ax, L[i][0], L[i][1], 2.2, r)
arrow(ax, sh(L[1], L[2], 3), sh(L[2], L[1], 3), 'varie', both=True)
text(ax, 22, 22, 'règle : inverse', 'varie', 's'); text(ax, 22, 14, '2 applications : retour', 'resultat', 's')
Rr = pts(66, 44, 11, 7)
for k, p in enumerate(Rr):
    disc(ax, p[0], p[1], 2.0, 'fixe' if k == 0 else ('varie' if k in (1, 2, 4) else 'autre'))
    q = pts(66, 44, 15.5, 7)[k]; text(ax, q[0], q[1], str(k), 'encre', 's')
for cyc, r in [((1, 2, 4), 'varie'), ((3, 6, 5), 'autre')]:
    for a in range(3):
        p, q = Rr[cyc[a]], Rr[cyc[(a + 1) % 3]]
        arrow(ax, sh(p, q, 2.8), sh(q, p, 2.8), r, curve=0.25)
text(ax, 66, 22, r'règle : $\times 2$ (exemple)', 'varie', 's'); text(ax, 66, 14, '3 applications : retour', 'resultat', 's')
save(fig, '50-260')
