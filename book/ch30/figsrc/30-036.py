import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
pi = math.pi
def pt(c, r, a): return (c[0] + r * math.cos(a), c[1] + r * math.sin(a))
def arc(ax, c, r, a0, a1, role='fixe', lw=0.9, dash=False, head=False, n=60):
    line(ax, [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
    if head:
        s = 1 if a1 > a0 else -1
        arrow(ax, pt(c, r, a1 - s * 0.12), pt(c, r, a1), role, lw)
def sq(ax, corner, d1, d2, s=2.2, role='fixe'):
    p1 = (corner[0] + d1[0] * s, corner[1] + d1[1] * s); p3 = (corner[0] + d2[0] * s, corner[1] + d2[1] * s)
    p2 = (p1[0] + d2[0] * s, p1[1] + d2[1] * s)
    line(ax, [p1, p2, p3], role, 0.7)
def dot(ax, p, role='sujet', r=1.1): disc(ax, p[0], p[1], r, role)

fig, ax = canvas(64)
y0 = 12; k = 28
line(ax, [(4, y0), (84, y0)], 'fixe', 0.8)
bars = [(14, 0.866, 'resultat', 'sin 120°'), (30, 0.866, 'autre', 'règle'), (52, 0.71, 'resultat', 'sin 135°'), (68, 1.22, 'limite', 'règle')]
for x, v, r, nm in bars:
    box(ax, x - 5, y0, 10, v * k, r, r=0.4)
    text(ax, x, y0 + v * k + 3, f'{v:g}'.replace('.', ','), r, 's')
    text(ax, x, y0 - 3, nm, r, 's')
text(ax, 22, y0 + 0.866 * k + 10, 'à 30° : pareil', 'encre', 's')
text(ax, 60, y0 + 1.22 * k + 8, 'à 45° : différent', 'encre', 's')
text(ax, 44, 3.5, r'règle = 1,732 $\times$ sinus de $x$', 'autre', 's')
save(fig, '30-036')
