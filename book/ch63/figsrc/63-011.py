import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
ox, oy, u = 16, 30, 14
arrow(ax, (4, oy), (82, oy), 'fixe')
text(ax, 70, 24, r'$\mathbb{Q}$ (axe)', 'fixe', 's')
text(ax, 62, 44, r'miroir $\sigma$', 'varie', 'm')
for a, lab_up, lab_dn in [(0, r'$\sqrt{2}$', r'$-\sqrt{2}$'), (1, r'$1+\sqrt{2}$', r'$1-\sqrt{2}$')]:
    x = ox + u * a
    disc(ax, x, oy + u, 1.7, 'sujet')
    disc(ax, x, oy - u, 1.7, 'varie')
    arrow(ax, (x, oy + u - 2.8), (x, oy - u + 2.8), 'varie')
    text(ax, x + 3, oy + u + 2, lab_up, 'sujet', 'm', ha='left')
    text(ax, x + 3, oy - u - 2, lab_dn, 'varie', 'm', ha='left')
disc(ax, ox + 2 * u, oy, 1.7, 'fixe')
text(ax, ox + 2 * u, oy + 4, '2', 'fixe', 'm')
save(fig, '63-011')
