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

fig, ax = canvas(72)
c = (26, 36); R = 22
disc(ax, *c, R, 'fixe', fill=False)
specs = [(0.5, 'autre', 'sécante', '2 points'), (1.0, 'sujet', 'tangente', '1 point'), (2.0, 'fixe', 'extérieure', '0 point')]
for d, r, nm, cnt in specs:
    x = c[0] + d * R
    line(ax, [(x, 12), (x, 60)], r, 1.5)
    text(ax, x, 7, nm, r, 's'); text(ax, x, 65, cnt, r, 's')
y = math.sqrt(1 - 0.25) * R
for sg in (-1, 1): dot(ax, (c[0] + 0.5 * R, c[1] + sg * y), 'autre', 1.3)
dot(ax, (c[0] + R, c[1]), 'sujet', 1.5)
dot(ax, c, 'fixe', 0.9)
text(ax, c[0] - 2.5, c[1] - 3, '$O$', 'encre', 's')
text(ax, c[0] + R - 1.5, c[1] + 3, '$A$', 'sujet', 's', ha='right')
save(fig, '30-045')
