import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, ay, ux, uy = 8, 42, 15, 4.5
arrow(ax, (6, ay), (70, ay), 'fixe', lw=0.8)
pts = [(ox + x * ux, ay + (x * x - 3 * x + 2) * uy) for x in [i / 20 for i in range(0, 73)]]
line(ax, pts, 'sujet', lw=1.4)
text(ax, 63, 61, r'$f$', 'sujet', 'm')
xs = ox + 3 * ux
line(ax, [(xs, ay), (xs, ay + 2 * uy)], 'resultat', lw=1.6)
text(ax, xs + 2, ay + uy, r'$f(3)=2$', 'resultat', 's', ha='left')
ax.plot([xs], [ay], 'o', color=COL['autre'], ms=3.5, zorder=5)
text(ax, xs, ay - 4, r'$s=3$', 'autre', 's')
for y, g, res, role in [(19, r'$g=y-3$ : $b_1=1$', r'$1^2\times2=2$', 'sujet'), (5, r'$g=2y-6$ : $b_1=2$', r'$2^2\times2=8$', 'autre')]:
    box(ax, 2, y, 38, 9, role, label=g, size='s')
    arrow(ax, (41, y + 4.5), (47, y + 4.5), 'varie')
    box(ax, 48, y, 38, 9, 'resultat', label=res, size='m')
save(fig, '70-050')
