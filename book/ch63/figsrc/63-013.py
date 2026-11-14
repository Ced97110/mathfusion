import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, u = 10, 30, 24
line(ax, [(4, oy), (82, oy)], 'resultat', lw=2.2)
for a, lab in [(0.5, '1/2'), (2, '2')]:
    x = ox + u * a
    disc(ax, x, oy, 1.8, 'resultat')
    text(ax, x, oy + 4.5, lab, 'resultat', 'm')
text(ax, 62, 23, r'points fixes : $\mathbb{Q}$', 'resultat', 's')
x = ox + u
disc(ax, x, oy + u, 1.8, 'sujet')
disc(ax, x, oy - u, 1.8, 'varie')
arrow(ax, (x, oy + u - 3), (x, oy - u + 3), 'varie')
text(ax, x + 4, oy + u, r'$1+\sqrt{2}$', 'sujet', 'm', ha='left')
text(ax, x + 4, oy - u, r'$1-\sqrt{2}$', 'varie', 'm', ha='left')
text(ax, x + 12, oy + 10, 'bouge', 'varie', 's')
save(fig, '63-013')
