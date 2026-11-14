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

fig, ax = canvas(56)
x0, x1, y = 8, 78, 12
f = numberline(ax, x0, x1, y, 0, 3, 1, arrow_right=False, every=1)
a, b = f(1), f(2.5708); hh = 0.5403 * 40
line(ax, [(a, y), (a, y + hh)], 'sujet', 2.2); line(ax, [(b, y), (b, y + hh)], 'resultat', 2.2)
line(ax, [(a, y + hh), (b, y + hh)], 'fixe', 0.8, dash=True)
dot(ax, (a, y), 'sujet'); dot(ax, (b, y), 'varie')
arrow(ax, (a + 1, y + 4), (b - 1, y + 4), 'varie', curve=-0.0)
text(ax, (a + b) / 2, y + 7.5, '+ 1,5708 (quart de tour)', 'varie', 's')
text(ax, a, y + hh + 4, r'$\cos 1$ = 0,5403', 'sujet', 's')
text(ax, b, y + hh + 4, r'$\sin 2{,}5708$ = 0,5403', 'resultat', 's')
text(ax, (a + b) / 2, y + hh + 4 + 7, 'même hauteur', 'fixe', 's')
save(fig, '30-035')
