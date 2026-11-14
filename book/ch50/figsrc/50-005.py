import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(cx, cy, R, n=12):
    return [(cx + R * math.cos(math.radians(90 - 360 / n * k)), cy + R * math.sin(math.radians(90 - 360 / n * k))) for k in range(n)]

fig, ax = canvas(55)
R, r = 11, 2.4
for cx, hrs, cap in [(22, [0, 4, 8], 'pas de 4 : 3 éléments'), (66, [0, 6], 'pas de 6 : 2 éléments')]:
    pts = ring(cx, 31, R)
    for k, p in enumerate(pts):
        if k in hrs: disc(ax, p[0], p[1], r, 'varie', label=str(k), size='s')
        else: disc(ax, p[0], p[1], 1.2, 'fixe')
    for a, b in zip(hrs, hrs[1:] + hrs[:1]):
        p, q = pts[a], pts[b]; dx, dy = q[0] - p[0], q[1] - p[1]; L = math.hypot(dx, dy)
        s = (r + 0.3) / L
        arrow(ax, (p[0] + dx * s, p[1] + dy * s), (q[0] - dx * s, q[1] - dy * s), 'sujet', lw=0.9)
    text(ax, cx, 13, cap, 'sujet', 's')
text(ax, 44, 5, r'pas de $12/d$ : $d$ éléments', 'resultat', 'm')
save(fig, '50-005')
