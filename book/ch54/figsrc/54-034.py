import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# repère : a (premier nombre) vers la droite, b (second) vers le haut
ox, oy = 12, 12
sx, sy = 9.0, 7.0
P = lambda a, b: (ox + a * sx, oy + b * sy)
arrow(ax, (ox - 4, oy), (ox + 8 * sx, oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy - 4), (ox, oy + 8.6 * sy), 'fixe', lw=0.9)
line(ax, [(ox - 4, oy), (ox + 7.8 * sx, oy)], 'limite', lw=1.4)
text(ax, ox + 8 * sx + 1, oy - 4, r'$a\in D$', 'fixe', 'm', ha='right')
text(ax, ox + 3, oy + 8.6 * sy, r'$b\in D^{*}$', 'fixe', 'm', ha='left')
for (a, b) in [(3, 5), (0, 7), (4, 1)]:
    x, y = P(a, b)
    disc(ax, x, y, 1.6, 'sujet')
    text(ax, x + 3, y + 3.2, f'({a}, {b})', 'sujet', 's', ha='left' if a else 'left')
x, y = P(3, 0)
disc(ax, x, y, 1.6, 'limite')
text(ax, x + 3, y + 3.2, '(3, 0)', 'limite', 's', ha='left')
text(ax, 62, 5, 'b = 0 : refusé', 'limite', 's')
save(fig, '54-034')
