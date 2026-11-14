import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
ox, oy, ua, ub = 8.0, 10.0, 4.2, 3.6
P = lambda a, b: (ox + a * ua, oy + b * ub)
arrow(ax, (ox, oy), (ox + 36, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy), (ox, oy + 44), 'fixe', lw=0.8)
text(ax, ox + 38.5, oy, r'$a$', 'fixe', 's')
text(ax, ox, oy + 46.5, r'$b$', 'fixe', 's')
line(ax, [P(0, 0), P(20 / 3, 10)], 'sujet', lw=1.3)
for a, b in [(2, 3), (4, 6), (6, 9)]:
    x, y = P(a, b)
    disc(ax, x, y, 1.3, 'varie')
    text(ax, x + 6, y - 2.2, f'({a}, {b})', 'varie', 's')
text(ax, 14, 56, 'la droite = la classe', 'sujet', 's', ha='left')
box(ax, 50, 36, 36, 10, 'resultat', label='[2, 3] = [4, 6]')
text(ax, 68, 31.5, 'vrai : même droite', 'resultat', 's')
box(ax, 50, 14, 36, 10, 'limite', label='(2, 3) = (4, 6)')
text(ax, 68, 9.5, 'faux : deux points', 'limite', 's')
save(fig, '54-068')
