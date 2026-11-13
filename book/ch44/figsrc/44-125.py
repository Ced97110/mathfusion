import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# 24 permutations, 8 of them are movements of the square
c = 7.0
for i in range(24):
    r, q = divmod(i, 8)
    good = i < 8
    ax.add_patch(Rectangle((2 + q * 10.5, 62 + (2 - r) * 0 - r * 9), 8.5, 7, ec=COL['sujet' if good else 'fixe'],
                 fc=FILL['sujet' if good else 'fixe'], lw=0.5, zorder=2))
text(ax, 44, 80, '24 réordonnements des coins', 'fixe', 's')
text(ax, 44, 40, '8 sont des mouvements du carreau', 'sujet', 's')
def square(x, y, labs, role):
    s = 14
    box(ax, x, y, s, s, role, lw=0.8, r=0.5)
    pos = [(x + 3.5, y + s - 3.5), (x + s - 3.5, y + s - 3.5), (x + s - 3.5, y + 3.5), (x + 3.5, y + 3.5)]
    for p, l in zip(pos, labs):
        text(ax, p[0], p[1], l, role, 's')
square(8, 14, '1234', 'sujet')
square(60, 14, '2134', 'limite')
arrow(ax, (24, 21), (58, 21), 'varie')
text(ax, 41, 26, 'échange 1 et 2', 'varie', 's')
text(ax, 41, 5, 'pas un mouvement du carreau', 'limite', 's')
save(fig, '44-125')
