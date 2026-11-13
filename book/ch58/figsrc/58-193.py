import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# couples d'entiers : la famille (2, 0), (0, 1) n'atteint pas (1, 0)
ox, oy, s = 12, 22, 14
text(ax, 44, 61, r'famille $(2, 0)$, $(0, 1)$ dans $\mathbb{Z}^2$', 'sujet', 'm', weight='bold')
for i in range(6):
    for j in range(3):
        if i % 2 == 0:
            disc(ax, ox + i * s, oy + j * s, 1.3, 'sujet')
        else:
            disc(ax, ox + i * s, oy + j * s, 1.3, 'limite', fill=False)
arrow(ax, (ox, oy), (ox + 2 * s - 2, oy), 'sujet', lw=1.6)
arrow(ax, (ox, oy), (ox, oy + s - 2), 'autre', lw=1.6)
text(ax, ox + s, oy + 4.5, r'$(2, 0)$', 'sujet', 's')
text(ax, ox - 2, oy + s / 2, r'$(0, 1)$', 'autre', 's', ha='right')
text(ax, ox + s, oy - 5, r'$(1, 0)$ hors d’atteinte', 'limite', 's', ha='left')
text(ax, 44, 8, r'il faudrait $\frac{1}{2} \times (2, 0)$ : pas un entier', 'limite', 's')
save(fig, '58-193')
