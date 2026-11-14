import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
x0, y0 = 10, 14
sx, sy = 40.0, 20.0            # 1 en x = 40 mm ; 1 en y = 20 mm
arrow(ax, (x0 - 3, y0), (x0 + 1.5 * sx, y0), 'fixe', lw=0.8)
arrow(ax, (x0, y0 - 3), (x0, y0 + 2.5 * sy), 'fixe', lw=0.8)
pts = [(x0 + t * sx, y0 + (t ** 5) * sy) for t in [i * 0.01 for i in range(0, 129)] if t ** 5 <= 2.35]
line(ax, pts, 'sujet', lw=1.5)
r = 2 ** 0.2
line(ax, [(x0, y0 + 2 * sy), (x0 + r * sx, y0 + 2 * sy)], 'fixe', lw=0.7, dash=True)
line(ax, [(x0 + r * sx, y0 + 2 * sy), (x0 + r * sx, y0)], 'resultat', lw=0.9, dash=True)
disc(ax, x0 + r * sx, y0 + 2 * sy, 1.5, 'resultat')
disc(ax, x0 + r * sx, y0, 1.5, 'resultat')
text(ax, x0 + 4, y0 + 2 * sy + 3, r'$y=2$', 'fixe', 's', ha='left')
text(ax, x0 + 33, y0 - 4.5, r'$1{,}15$', 'resultat', 's', ha='right')
text(ax, 70, 56, r'$y=x^5$', 'sujet', 'm')
text(ax, 68, 40, 'racine réelle', 'resultat', 's')
text(ax, 68, 34, 'un seul radical', 'resultat', 's')
text(ax, 68, 22, r'$1{,}15^5\approx2{,}01$', 'encre', 's')
save(fig, '65-130')
