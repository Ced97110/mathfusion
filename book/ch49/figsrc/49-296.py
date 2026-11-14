import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 44, 95, r'$\mathbb{Z}$ : aucune relation', 'sujet', 'm', weight='bold')
f = numberline(ax, 10, 70, 78, 0, 5, labels=False, arrow_right=True)
for v, lab in [(0, '0'), (1, '1'), (5, '5')]:
    text(ax, f(v), 71.5, lab, 'fixe', 's')
text(ax, f(1), 66, r'$x$', 'sujet', 'm'); text(ax, f(5), 66, r'$x^5$', 'resultat', 'm')
arrow(ax, (f(0), 80), (f(5), 80), 'varie', curve=-0.25)
text(ax, f(2.5), 88.5, '5 fois : on arrive à 5', 'resultat', 's')
line(ax, [(5, 59.5), (83, 59.5)], 'fixe', dash=True)
text(ax, 44, 55, r'$\mathbb{Z}/5\mathbb{Z}$ : une relation', 'limite', 'm', weight='bold')
c = (44, 28); R = 17
pts = []
for i in range(5):
    a = math.radians(90 - 72 * i)
    pts.append((c[0] + R * math.cos(a), c[1] + R * math.sin(a)))
for i in range(5):
    a, b = pts[i], pts[(i + 1) % 5]
    d = math.hypot(b[0]-a[0], b[1]-a[1]); u = ((b[0]-a[0])/d, (b[1]-a[1])/d)
    arrow(ax, (a[0]+u[0]*4.2, a[1]+u[1]*4.2), (b[0]-u[0]*4.2, b[1]-u[1]*4.2), 'limite' if i == 4 else 'varie')
for i, p in enumerate(pts):
    disc(ax, p[0], p[1], 3.4, 'fixe', label=str(i))
text(ax, 44, 28, '5 fois : 0', 'limite', 's')
save(fig, '49-296')
