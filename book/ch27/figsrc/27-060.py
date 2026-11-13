import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
gy = 14; x0 = 8
line(ax, [(x0, gy), (82, gy)], 'fixe', lw=1.4)
th = math.radians(20)
for phi in (30, 50, 70):
    a = math.atan(math.tan(th) * math.cos(math.radians(phi)))
    line(ax, [(x0, gy), (x0 + 66 * math.cos(a), gy + 66 * math.sin(a))], 'fixe', lw=1.0)
pts = [(x0, gy)] + [(x0 + 22 * math.cos(th * k / 14), gy + 22 * math.sin(th * k / 14)) for k in range(15)]
poly(ax, pts, 'sujet', lw=0.5)
line(ax, [(x0, gy), (x0 + 66 * math.cos(th), gy + 66 * math.sin(th))], 'sujet', lw=2.4)
text(ax, x0 + 30, gy + 6.2, r'$\theta$ = 20°', 'sujet', 'l')
text(ax, 78, gy + 31, 'pente maximale', 'sujet', 's', ha='right')
text(ax, 78, gy + 27.5, 'plus grande pente', 'sujet', 's', ha='right')
text(ax, 84, gy + 10, 'autres chemins :', 'fixe', 's', ha='right')
text(ax, 84, gy + 6.6, 'moins raides', 'fixe', 's', ha='right')
text(ax, 44, 7, 'colline vue de côté', 'fixe', 's')
save(fig, '27-060')
