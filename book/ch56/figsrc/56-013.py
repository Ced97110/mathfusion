import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 54, r'$N(a+b\sqrt{-5}) = a^2 + 5b^2 = d^2$', 'encre', 'l')
text(ax, 44, 47, 'd : distance du point à 0', 'encre', 's')
ox, oy, u = 8, 13, 9
s5 = 5 ** 0.5
arrow(ax, (3, oy), (38, oy), 'fixe', lw=0.7)
# repères du point 1 + √−5 : a = 1 et hauteur √5
line(ax, [(ox + u, oy), (ox + u, oy + s5 * u)], 'fixe', dash=True)
for (a, b, role) in [(2, 0, 'sujet'), (3, 0, 'autre'), (1, 1, 'varie')]:
    px, py = ox + a * u, oy + b * s5 * u
    line(ax, [(ox, oy), (px, py)], role, lw=1.0)
    disc(ax, px, py, 1.3, role)
disc(ax, ox, oy, 1.1, 'encre')
text(ax, ox, oy - 4, '0', 'encre', 's')
text(ax, ox + 2 * u, oy - 4, '2', 'sujet', 's')
text(ax, ox + 3 * u, oy - 4, '3', 'autre', 's')
text(ax, ox + u + 3, oy - 4, 'a = 1', 'fixe', 's', ha='right')
text(ax, ox + u + 1.5, oy + s5 * u / 2, r'$\sqrt{5}$', 'fixe', 's', ha='left')
text(ax, ox + u + 1, oy + s5 * u + 4, '1 + √−5', 'varie', 's', ha='left')
text(ax, ox + 3, oy + s5 * u / 2 + 4, '$d$', 'varie', 's')
text(ax, 44, 34, 'N(2) = 2² + 5·0² = 4', 'sujet', 's', ha='left')
text(ax, 44, 25, 'N(1 + √−5) = 1 + 5 = 6', 'varie', 's', ha='left')
text(ax, 44, 16, 'N(3) = 3² + 5·0² = 9', 'autre', 's', ha='left')
save(fig, '56-013')
