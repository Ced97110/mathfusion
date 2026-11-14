import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
R = 2.9
xs = [24 + 10 * i for i in range(7)]
yt, yb = 50, 20

def edge(p, q, r):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    return (p[0] + dx / d * r, p[1] + dy / d * r)

def hop(i, j, y, role, both=False):
    p, q = (xs[i], y), (xs[j], y)
    arrow(ax, edge(p, q, R), edge(q, p, R), role, both=both)

text(ax, 7, yt, r'$\sigma$', 'sujet', 'xl')
text(ax, 7, yb, r'$\sigma^2$', 'resultat', 'xl')

# sigma = (1 2)(3 4)(5 6 7)
for i in range(4):
    disc(ax, xs[i], yt, R, 'varie', label=str(i + 1))
for i in range(4, 7):
    disc(ax, xs[i], yt, R, 'sujet', label=str(i + 1))
hop(0, 1, yt, 'varie', both=True)
hop(2, 3, yt, 'varie', both=True)
hop(4, 5, yt, 'sujet')
hop(5, 6, yt, 'sujet')
arrow(ax, (xs[6], yt + R), (xs[4], yt + R), 'sujet', curve=0.4)

# sigma^2 : échanges annulés, 3-cycle au carré (5 7 6)
for i in range(4):
    disc(ax, xs[i], yb, R, 'fixe')
for i in range(4, 7):
    disc(ax, xs[i], yb, R, 'resultat', label=str(i + 1))
arrow(ax, (xs[4], yb - R), (xs[6], yb - R), 'resultat', curve=0.5)
hop(6, 5, yb, 'resultat')
hop(5, 4, yb, 'resultat')
text(ax, 39, 9, 'échanges annulés', 'fixe', 's')
text(ax, 74, 9, 'cycle au carré', 'resultat', 's')
save(fig, '64-132')
