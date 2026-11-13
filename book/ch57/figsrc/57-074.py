import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, r'$x,\ y\in M$', 'sujet', 'l', weight='bold')
box(ax, 3, 3, 46, 46, 'fixe', fill=False, dash=True)
ox, oy, u = 9, 9, 7
for i in range(6):
    for j in range(6):
        if (i, j) in [(2, 1), (1, 4)]: continue
        disc(ax, ox + u * i, oy + u * j, 0.9, 'fixe')
px, py = ox + 2 * u, oy + 1 * u
qx, qy = ox + 1 * u, oy + 4 * u
disc(ax, px, py, 2, 'sujet'); disc(ax, qx, qy, 2, 'sujet')
line(ax, [(px + 2, py), (52, py)], 'sujet'); line(ax, [(qx + 2, qy), (52, qy)], 'sujet')
text(ax, 54, py, 'x = (2 ; 1)', 'sujet', 's', ha='left')
text(ax, 54, qy, 'y = (1 ; 4)', 'sujet', 's', ha='left')
text(ax, 68, 46, "M : les couples\nd'entiers", 'fixe', 's')
save(fig, '57-074')
