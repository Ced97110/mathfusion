import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, u = 28, 33, 11
four = {(1, 0), (-1, 0), (0, 1), (0, -1)}
for i in range(-2, 3):
    for j in range(-2, 3):
        if (i, j) in four: disc(ax, cx + i*u, cy + j*u, 1.5, 'varie')
        else: disc(ax, cx + i*u, cy + j*u, 0.7, 'fixe')
ax.add_patch(Circle((cx, cy), u, fill=False, ec=COL['varie'], lw=0.7, ls='--', zorder=1))
arrow(ax, (cx, cy), (cx + u - 1.8, cy), 'sujet', lw=1.3)
arrow(ax, (cx, cy), (cx, cy + u - 1.8), 'autre', lw=1.3)
text(ax, cx + 5.5, cy - 3, r'$x$', 'sujet', 'm')
text(ax, cx - 3, cy + 5.5, r'$y$', 'autre', 'm')
text(ax, 58, 52, '4 points à', 'varie', 's', ha='left')
text(ax, 58, 48.5, 'distance 1', 'varie', 's', ha='left')
text(ax, 58, 38, 'x : 4 choix', 'sujet', 's', ha='left')
text(ax, 58, 33, 'y : 4 choix', 'autre', 's', ha='left')
box(ax, 57, 15, 28, 10, 'resultat', label='au plus 16 : fini', size='s')
text(ax, 44, 5, 'points du réseau dans un disque', 'fixe', 's')
save(fig, '74-084')
