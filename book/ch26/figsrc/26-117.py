import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(62)
O = (44, 20); R = 30
ax.add_patch(Polygon([O] + [pol(O, R, 30 * i / 10) for i in range(11)], closed=True, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=2))
arc(ax, O, R, 0, 180, 'encre', lw=1.0)
line(ax, [pol(O, R, 180), pol(O, R, 0)], 'encre', lw=1.0)
for k in range(1, 6): line(ax, [O, pol(O, R, 30 * k)], 'fixe', lw=0.7)
for k in range(7): text(ax, *pol(O, R + 5.2, 30 * k), f'{30 * k}°', 'sujet' if k == 1 else 'encre', 's')
text(ax, 44, 9.5, '30° = un sixième de demi-tour', 'sujet', 's')
text(ax, 44, 4, r'$\pi/6\approx 0{,}5236$ rad', 'varie', 's')
text(ax, 44, 33, 'demi-tour', 'encre', 's')
save(fig, '26-117')
