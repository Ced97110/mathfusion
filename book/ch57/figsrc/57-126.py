import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 7.2; ox, oy = 44.0, 31.0
P = lambda x, y: (ox + x * u, oy + y * u)
blue = {(0, 0), (2, 1), (4, 2), (-2, -1), (-4, -2)}
for i in range(-5, 6):
    for j in range(-3, 4):
        if (i, j) in blue or (i, j) == (1, 1): continue
        disc(ax, *P(i, j), 0.55, 'fixe')
arrow(ax, P(0, 0), (P(2, 1)[0] - 1.2, P(2, 1)[1] - 0.6), 'sujet', lw=1.3)
for (i, j) in blue:
    disc(ax, *P(i, j), 1.2, 'sujet')
q = P(1, 1)
ax.add_patch(Rectangle((q[0] - 1.5, q[1] - 1.5), 3, 3, ec=COL['limite'], fc=FILL['limite'], lw=0.9, zorder=3))
text(ax, P(2, 1)[0] + 1, P(2, 1)[1] + 4.2, r'$u=(2\,;\,1)$', 'sujet', 's')
text(ax, q[0] - 8, q[1] + 3.5, r'$(1\,;\,1)\notin N$', 'limite', 's')
text(ax, 22, 5, r'gris : $\mathbb{Z}^2$', 'fixe', 's')
text(ax, 64, 5, r'bleu : $N=\mathbb{Z}u$', 'sujet', 's')
save(fig, '57-126')
