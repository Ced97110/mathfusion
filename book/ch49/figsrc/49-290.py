import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def ring(cx, cy, R, labels, role, start=225):
    n = len(labels); P = []
    for i in range(n):
        a = math.radians(start - 360 / n * i)
        P.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    return P
# square (left)
P = [(14, 38), (34, 38), (34, 58), (14, 58)]
poly(ax, P, 'fixe')
for i, p in enumerate(P):
    disc(ax, p[0], p[1], 3.6, 'sujet', label=str(i + 1))
for i in range(4):
    a, b = P[i], P[(i + 1) % 4]
    d = math.hypot(b[0]-a[0], b[1]-a[1]); u = ((b[0]-a[0])/d, (b[1]-a[1])/d)
    arrow(ax, (a[0]+u[0]*5, a[1]+u[1]*5), (b[0]-u[0]*5, b[1]-u[1]*5), 'varie')
text(ax, 24, 29, 'sur ses 4 sommets', 'sujet', 's')
# group on itself (right)
labs = ['$e$', '$r$', '$r^2$', '$r^3$']
c = (65, 48); Q = [(c[0] - 9, c[1] - 9), (c[0] + 9, c[1] - 9), (c[0] + 9, c[1] + 9), (c[0] - 9, c[1] + 9)]
for i, p in enumerate(Q):
    disc(ax, p[0], p[1], 4.0, 'autre', label=labs[i])
for i in range(4):
    a, b = Q[i], Q[(i + 1) % 4]
    d = math.hypot(b[0]-a[0], b[1]-a[1]); u = ((b[0]-a[0])/d, (b[1]-a[1])/d)
    arrow(ax, (a[0]+u[0]*5.5, a[1]+u[1]*5.5), (b[0]-u[0]*5.5, b[1]-u[1]*5.5), 'varie')
text(ax, 65, 29, 'sur lui-même', 'autre', 's')
text(ax, 65, 62.5, '', 'autre', 's')
box(ax, 8, 4, 72, 17, 'resultat')
text(ax, 44, 15, 'une seule orbite : 4 éléments', 'resultat', 'm')
text(ax, 44, 8.5, 'seul le neutre fixe un point', 'resultat', 's')
save(fig, '49-290')
