import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, sx, sy = 44, 18, 11, 5.5
pts = [(ox + t * sx, oy + (t * t - 2) * sy) for t in [i / 20 * 3.2 - 1.6 for i in range(21)]]
pts = [(ox + (i / 20 * 6.4 - 3.2) * sx, oy + ((i / 20 * 6.4 - 3.2) ** 2 - 2) * sy) for i in range(21)]
pts = [(x, y) for x, y in pts if y > 3 and y < 56 and 4 < x < 84]
line(ax, pts, 'sujet', lw=1.2)
arrow(ax, (4, oy), (82, oy), 'fixe', lw=0.8)
r2 = ox + 1.4142 * sx
line(ax, [(ox + 0, oy + (0 - 2) * sy), (ox, oy + (0 - 2) * sy)], 'fixe')
disc(ax, r2, oy, 1.6, 'resultat')
text(ax, r2 + 2, oy - 5, r'$\sqrt{2}$', 'resultat', 'l')
text(ax, 22, 52, r'$x^2-2$', 'sujet', 'l', weight='bold')
text(ax, r2 + 4, oy + 8, 'vaut 0 ici', 'resultat', 's', ha='left')
text(ax, 44, 4, r'$\sqrt{2}$ annule le polynôme', 'resultat', 'm')
save(fig, '61-050')
