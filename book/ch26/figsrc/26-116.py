import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(68)
O = (28, 30); R = 24
ax.add_patch(Circle(O, R, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=1.5))
arrow(ax, (O[0] - R - 3, O[1]), (O[0] + R + 5, O[1]), 'fixe', lw=0.7)
arrow(ax, (O[0], O[1] - 3), (O[0], O[1] + R + 5), 'fixe', lw=0.7)
line(ax, [O, (O[0], O[1] + R)], 'encre', lw=1.0); text(ax, O[0] - 3.5, O[1] + 12, '1', 'encre', 's')
disc(ax, O[0] + R, O[1], 1.7, 'autre'); disc(ax, O[0], O[1] + R, 1.7, 'varie')
arc(ax, O, 8, 0, 90, 'varie'); text(ax, O[0] + 12.5, O[1] + 10, '90°', 'varie', 's')
text(ax, O[0] + R + 2, O[1] - 4, '(1, 0)', 'autre', 's')
text(ax, O[0] + 12, O[1] + R + 5, '(0, 1)', 'varie', 's')
text(ax, 71, 34, 'à 0°', 'autre', 's', weight='bold')
text(ax, 71, 29, r'$\cos 0°=1$', 'autre', 's'); text(ax, 71, 24, r'$\sin 0°=0$', 'autre', 's')
text(ax, 71, 60, 'à 90°', 'varie', 's', weight='bold')
text(ax, 71, 55, r'$\cos 90°=0$', 'varie', 's'); text(ax, 71, 50, r'$\sin 90°=1$', 'varie', 's')
save(fig, '26-116')
