import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
u = 5.6; oy = 24.0
def panel(ox, real):
    P = lambda x, y: (ox + x * u, oy + y * u)
    for i in range(-2, 6):
        for j in range(-1, 4):
            if (i, j) in ((0, 0), (2, 1), (4, 2), (-2, -1), (1, 1)): continue
            disc(ax, *P(i, j), 0.4, 'fixe')
    if real:
        line(ax, [P(-2, -1), P(5, 2.5)], 'sujet', lw=1.4)
    for k in (-1, 0, 1, 2):
        disc(ax, *P(2 * k, k), 1.1, 'sujet')
    q = P(1, 1)
    ax.add_patch(Rectangle((q[0] - 1.1, q[1] - 1.1), 2.2, 2.2, ec=COL['limite'], fc=FILL['limite'], lw=0.8, zorder=3))
    return P
panel(15, False)
P = panel(58, True)
for (x, y) in ((1, 0.5), (3, 1.5)):
    disc(ax, *P(x, y), 1.1, 'varie')
text(ax, P(1, 0.5)[0] + 2, P(1, 0.5)[1] - 3.8, r'$\frac{1}{2}u$', 'varie', 's')
text(ax, P(3, 1.5)[0] + 1, P(3, 1.5)[1] - 4.2, r'$1{,}5\,u$', 'varie', 's')
text(ax, P(1, 1)[0] - 4, P(1, 1)[1] + 4.2, r'$(1\,;\,1)$', 'limite', 's')
text(ax, 22, 50, 'coefficients entiers', 'sujet', 's')
text(ax, 64, 50, 'coefficients réels', 'sujet', 's')
text(ax, 22, 8, 'points isolés', 'sujet', 's')
text(ax, 64, 8, 'toute la droite', 'sujet', 's')
save(fig, '57-129')
