import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(74)
X0, Y0, SX, SY = 14, 24, 0.6, 38
fx = lambda d: X0 + d * SX
fy = lambda v: Y0 + v * SY
arrow(ax, (X0 - 2, Y0), (fx(90) + 4, Y0), 'fixe', lw=0.8); arrow(ax, (X0, Y0 - 2), (X0, fy(1) + 6), 'fixe', lw=0.8)
ds = [i * 3 for i in range(31)]
line(ax, [(fx(d), fy(math.sin(math.radians(d)))) for d in ds], 'sujet', lw=1.4)
line(ax, [(fx(d), fy(math.cos(math.radians(d)))) for d in ds], 'autre', lw=1.4)
for d in (0, 30, 60, 90):
    text(ax, fx(d), Y0 - 3.5, f'{d}°', 'encre', 's')
text(ax, X0 - 3.5, fy(1), '1', 'encre', 's')
sv = [0, 0.5, 0.866, 1.0]
for i in range(1, 4):
    d = 30 * i
    line(ax, [(fx(d - 30), fy(sv[i - 1])), (fx(d), fy(sv[i - 1]))], 'fixe', dash=True, lw=0.6)
    arrow(ax, (fx(d), fy(sv[i - 1])), (fx(d), fy(sv[i])), 'varie', lw=1.0)
    disc(ax, fx(d), fy(sv[i]), 1.0, 'sujet')
text(ax, fx(30) + 8, fy(0.25), '+0,5', 'varie', 's')
text(ax, fx(60) + 9, fy(0.68), '+0,366', 'varie', 's')
text(ax, fx(90) + 9, fy(0.93), '+0,134', 'varie', 's')
line(ax, [(fx(30), fy(0.866)), (fx(60), fy(0.866))], 'resultat', lw=1.0, dash=True)
disc(ax, fx(30), fy(0.866), 1.0, 'autre')
text(ax, fx(45), fy(0.866) + 3.8, '0,866', 'resultat', 's', weight='bold')
text(ax, fx(10), fy(0.5), 'sin', 'sujet', 'm', weight='bold')
text(ax, fx(80), fy(0.5), 'cos', 'autre', 'm', weight='bold')
arrow(ax, (fx(0), Y0 - 9), (fx(90), Y0 - 9), 'sujet', lw=1.2)
text(ax, fx(45), Y0 - 12.2, 'sin : lu de gauche à droite', 'sujet', 's')
arrow(ax, (fx(90), Y0 - 17), (fx(0), Y0 - 17), 'autre', lw=1.2)
text(ax, fx(45), Y0 - 20.2, 'cos : lu de droite à gauche', 'autre', 's')
save(fig, '26-118')
