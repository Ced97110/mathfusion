import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
R = 3.2
xs = [20 + 15 * i for i in range(5)]
y1, y2, y3 = 76, 46, 16

def edge(p, q, r):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    return (p[0] + dx / d * r, p[1] + dy / d * r)

def hop(i, j, y, role, both=False):
    p, q = (xs[i], y), (xs[j], y)
    arrow(ax, edge(p, q, R), edge(q, p, R), role, both=both)

def ghost(y):
    ax.add_patch(Circle((xs[4], y), R, ec=COL['fixe'], fc='none', lw=0.8, ls='--', zorder=2))

# ligne 1 : sigma = (1 2)(3 4)
text(ax, 6, y1, r'$\sigma$', 'sujet', 'xl')
for i in range(4):
    disc(ax, xs[i], y1, R, 'sujet', label=str(i + 1))
ghost(y1)
hop(0, 1, y1, 'sujet', both=True)
hop(2, 3, y1, 'sujet', both=True)

# ligne 2 : pi = (1 3)(2 4)
text(ax, 6, y2, r'$\pi$', 'varie', 'xl')
for i in range(4):
    disc(ax, xs[i], y2, R, 'varie', label=str(i + 1))
ghost(y2)
arrow(ax, (xs[0], y2 + R), (xs[2], y2 + R), 'varie', curve=-0.45, both=True)
arrow(ax, (xs[1], y2 - R), (xs[3], y2 - R), 'varie', curve=0.45, both=True)

# ligne 3 : mu = (1 3 5) avec le cinquième objet
text(ax, 6, y3, r'$\mu$', 'resultat', 'xl')
disc(ax, xs[0], y3, R, 'resultat', label='1')
disc(ax, xs[1], y3, R, 'fixe')
disc(ax, xs[2], y3, R, 'resultat', label='3')
disc(ax, xs[3], y3, R, 'fixe')
disc(ax, xs[4], y3, R, 'varie', label='5')
arrow(ax, (xs[0], y3 + R), (xs[2], y3 + R), 'resultat', curve=-0.45)
arrow(ax, (xs[2], y3 + R), (xs[4], y3 + R), 'resultat', curve=-0.45)
arrow(ax, (xs[4], y3 - R), (xs[0], y3 - R), 'resultat', curve=-0.3)

# passages d'une ligne à l'autre
arrow(ax, (12, y1 - 5), (12, y2 + 5), 'fixe', lw=0.7)
arrow(ax, (12, y2 - 5), (12, y3 + 5), 'fixe', lw=0.7)
save(fig, '64-133')
