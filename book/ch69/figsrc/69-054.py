import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
u = 12; ox, oy = 12, 12
arrow(ax, (ox, oy), (ox + 50, oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy), (ox, oy + 42), 'fixe', lw=0.9)
for k in (1, 2, 3):
    line(ax, [(ox + k * u, oy - 1), (ox + k * u, oy + 1)], 'fixe')
    text(ax, ox + k * u, oy - 4, str(k), 'fixe', 's')
for k in (1, 2):
    line(ax, [(ox - 1, oy + k * u), (ox + 1, oy + k * u)], 'fixe')
    text(ax, ox - 4, oy + k * u, str(k), 'fixe', 's')
px, py = ox + 3 * u, oy + 2 * u
line(ax, [(px, oy), (px, py)], 'fixe', lw=0.6, dash=True)
line(ax, [(ox, py), (px, py)], 'fixe', lw=0.6, dash=True)
disc(ax, px, py, 1.8, 'sujet')
text(ax, px + 3, py + 4, r'$3+2i$', 'sujet', 's', ha='left')
text(ax, 72, oy + 3, r'$a\in R$', 'sujet', 's')
text(ax, ox + 2, 58, r'$b\in R$, devant $i$', 'sujet', 's', ha='left')
box(ax, 62, 28, 24, 10, 'varie', label=r'$i^2=-1$', size='s')
save(fig, '69-054')
