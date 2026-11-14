import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 11.0; ox, oy = 12, 12
for m in range(0, 6):
    for n in range(0, 4):
        disc(ax, ox + m * u, oy + n * u, 0.8, 'fixe')
arrow(ax, (ox - 5, oy), (ox + 5.6 * u, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 4), (ox, oy + 3.6 * u), 'fixe', lw=0.7)
px, py = ox + 3 * u, oy + 2 * u
line(ax, [(px, oy), (px, py)], 'varie', dash=True)
line(ax, [(ox, py), (px, py)], 'varie', dash=True)
disc(ax, px, py, 1.8, 'sujet')
text(ax, px + 2.5, py + 3.5, r'$3+2i$', 'sujet', 'm', ha='left')
text(ax, px, oy - 4, r'$m=3$', 'varie', 's')
text(ax, ox - 2.5, py, r'$n=2$', 'varie', 's', ha='right')
text(ax, ox - 2.5, oy - 3.5, '0', 'fixe', 's', ha='right')
box(ax, 64, 50, 22, 9, 'autre', label=r'$i^2=-1$')
text(ax, 70, 5, 'cases de côté 1', 'fixe', 's')
save(fig, '56-125')
