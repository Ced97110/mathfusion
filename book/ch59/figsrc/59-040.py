import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def tb(ax, x, y, s, role, size='s'):
    ax.text(x, y, s, color=COL[role], fontsize=SIZE[size], ha='center', va='center', zorder=5, bbox=dict(fc='white', ec='none', pad=0.6))
ox, oy, u = 10, 10, 7.2
P = lambda a, b: (ox + a * u, oy + b * u)
K = {(4 * a + 6 * b, 6 * a + 4 * b) for a in range(-5, 6) for b in range(-5, 6)}
for a in range(7):
    for b in range(7):
        inK = (a, b) in K
        disc(ax, *P(a, b), 1.4 if inK else 0.5, 'sujet' if inK else 'fixe')
line(ax, [P(0, 0), P(4, 0), P(4, 6)], 'varie', lw=1.2, dash=True)
tb(ax, *P(2, -0.8), r'4 fois $x_1$', 'varie', 's')
tb(ax, P(4, 3)[0] + 8.5, P(4, 3)[1], r'6 fois $x_2$', 'varie', 's')
text(ax, *P(3.0, 6.75), r'(4, 6) $\in K$', 'sujet', 's')
text(ax, P(6, 4)[0] + 1.8, P(6, 4)[1], r'(6, 4) $\in K$', 'sujet', 's', ha='left')
text(ax, *P(-0.1, -0.8), r'(0, 0)', 'sujet', 's')
box(ax, 58, 46, 28, 13, 'resultat', label='$4x_1+6x_2=0$\ndans $M$', size='s')
arrow(ax, (P(4, 6)[0] + 2.2, P(4, 6)[1]), (57.4, 52.5), 'resultat')
save(fig, '59-040')
