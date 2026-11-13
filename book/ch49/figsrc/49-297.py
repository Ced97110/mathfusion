import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
c = (34, 38); R = 24
labs = ['$1$', '$x$', '$x^2$', '$x^3$', '$x^4$']
pts = []
for i in range(5):
    a = math.radians(90 - 72 * i)
    pts.append((c[0] + R * math.cos(a), c[1] + R * math.sin(a)))
for i in range(5):
    a, b = pts[i], pts[(i + 1) % 5]
    d = math.hypot(b[0]-a[0], b[1]-a[1]); u = ((b[0]-a[0])/d, (b[1]-a[1])/d)
    arrow(ax, (a[0]+u[0]*5.2, a[1]+u[1]*5.2), (b[0]-u[0]*5.2, b[1]-u[1]*5.2), 'resultat' if i == 4 else 'varie')
for i, p in enumerate(pts):
    disc(ax, p[0], p[1], 4.6, 'sujet', label=labs[i])
text(ax, 34, 38, '5 éléments', 'sujet', 'm')
text(ax, 34, 32, 'on recommence', 'varie', 's')
box(ax, 62, 50, 24, 9, 'limite', label=r'$x^5 = 1$', size='m')
box(ax, 62, 36, 24, 9, 'resultat', label=r'$x^6 = x$', size='m')
text(ax, 74, 64, 'la relation', 'limite', 's')
text(ax, 74, 28, 'on boucle', 'resultat', 's')
save(fig, '49-297')
