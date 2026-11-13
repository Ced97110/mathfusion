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

fig, ax = canvas(70)
x0, wd, cy, A = 10, 66, 36, 16
X = lambda t: x0 + t / (2 * pi) * wd
ts = [i * 2 * pi / 120 for i in range(121)]
line(ax, [(x0 - 3, cy), (x0 + wd + 4, cy)], 'fixe', 0.6)
for v in (0, pi / 2, pi, 3 * pi / 2, 2 * pi):
    line(ax, [(X(v), 8), (X(v), 62)], 'fixe', 0.4, dash=True)
line(ax, [(X(t), cy + A * math.sin(t)) for t in ts], 'autre', 1.3)
line(ax, [(X(t), cy + A * math.cos(t)) for t in ts], 'sujet', 1.5)
for v, lab in ((0, '0'), (pi / 2, r'$\pi/2$'), (pi, r'$\pi$'), (3 * pi / 2, r'$3\pi/2$'), (2 * pi, r'$2\pi$')):
    text(ax, X(v), 4.5, lab, 'fixe', 's')
dot(ax, (X(0), cy + A), 'sujet'); dot(ax, (X(pi / 2), cy + A), 'autre')
dot(ax, (X(pi), cy - A), 'sujet'); dot(ax, (X(3 * pi / 2), cy - A), 'autre')
arrow(ax, (X(0) + 1.8, cy + A), (X(pi / 2) - 1.8, cy + A), 'varie')
arrow(ax, (X(pi) + 1.8, cy - A), (X(3 * pi / 2) - 1.8, cy - A), 'varie')
text(ax, X(pi / 4), cy + A + 3, r'$+\pi/2$', 'varie', 's'); text(ax, X(5 * pi / 4), cy - A - 3, r'$+\pi/2$', 'varie', 's')
text(ax, X(pi / 2) + 13, cy + 21, 'sinus', 'autre', 's'); text(ax, X(2 * pi) - 4, cy + 21, 'cosinus', 'sujet', 's')
text(ax, 44, 67, r'cosinus $\pi/2$ plus tôt que sinus', 'encre', 'm', weight='bold')
save(fig, '30-037')
