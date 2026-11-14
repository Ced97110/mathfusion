import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(64)
x0, x1, oy, k = 14, 78, 30, 4.0
fx = lambda d: x0 + d / 90 * (x1 - x0)
fy = lambda v: oy + v * k
line(ax, [(x0, oy), (x1 + 4, oy)], 'fixe', lw=0.7); line(ax, [(x0, 6), (x0, 56)], 'fixe', lw=0.7)
line(ax, [(fx(d), fy(5 * math.cos(math.radians(d + 53.13)))) for d in range(0, 91, 3)], 'sujet', lw=1.5)
disc(ax, fx(0), fy(3), 1.4, 'resultat'); disc(ax, fx(90), fy(-4), 1.4, 'resultat')
line(ax, [(fx(0), fy(3)), (fx(0), oy)], 'resultat', 0.6, True); line(ax, [(fx(90), fy(-4)), (fx(90), oy)], 'resultat', 0.6, True)
text(ax, fx(0) + 3, fy(3) + 3.5, '3 à 0°', 'resultat', 's', ha='left', weight='bold'); text(ax, fx(90) - 2, fy(-4) - 3.5, '−4 à 90°', 'resultat', 's', ha='right', weight='bold')
text(ax, fx(0) + 3, oy - 3, '0°', 'fixe', 's'); text(ax, fx(90), oy + 3.5, '90°', 'fixe', 's')
text(ax, 44, 60, r'$3\cos x-4\sin x=5\cos(x+53{,}13^\circ)$', 'sujet', 's')
text(ax, 50, 3.5, 'mêmes valeurs aux deux angles', 'resultat', 's')
save(fig, '35-046')
