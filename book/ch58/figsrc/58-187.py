import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# chaque nombre a + b√2 est un point (a, b) : deux coordonnées, deux fractions
ox, oy, ux, uy = 14, 12, 15.0, 10.0
arrow(ax, (ox, oy), (ox + 4.3 * ux, oy), 'fixe', lw=0.9)
arrow(ax, (ox, oy), (ox, oy + 5.9 * uy), 'fixe', lw=0.9)
text(ax, ox + 4.3 * ux - 1, oy - 3.5, r'$a$ (sur 1)', 'sujet', 's', ha='right')
text(ax, ox + 2, oy + 5.9 * uy + 2.5, r'$b$ (sur $\sqrt{2}$)', 'autre', 's', ha='left')
pts = [(3, 1, r'$3 + \sqrt{2}$', '3', '1'), (0.5, 5, r'$\frac{1}{2} + 5\sqrt{2}$', '1/2', '5')]
for a, b, lab, ta, tb in pts:
    px, py = ox + a * ux, oy + b * uy
    line(ax, [(px, oy), (px, py)], 'fixe', dash=True, lw=0.6)
    line(ax, [(ox, py), (px, py)], 'fixe', dash=True, lw=0.6)
    disc(ax, px, py, 1.2, 'varie')
    text(ax, ox + a * ux, oy - 3.5 if a > 1 else oy - 3.5, ta, 'sujet', 's')
    text(ax, ox - 3, py, tb, 'autre', 's', ha='right')
    text(ax, px + 2.5, py + 3, lab, 'varie', 's', ha='left')
text(ax, 58, 42,r'$\dim = 2$ sur $\mathbb{Q}$', 'resultat', 'm', weight='bold')
save(fig, '58-187')
