import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# left : sqrt(2) on a line
f = numberline(ax, 6, 30, 38, 0, 2, step=1, arrow_right=False)
disc(ax, f(2 ** 0.5), 38, 1.6, 'sujet')
text(ax, f(2 ** 0.5), 44, r'$\sqrt{2}$', 'sujet', 'm')
text(ax, 20, 50, 'nombre réel', 'fixe', 's')
text(ax, 20, 28, r'annule $x^2-2$', 'sujet', 's')
# right : pentagon on the unit circle
cx, cy, R = 64, 35, 16
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.6)
import math
P = [(cx + R * math.cos(math.radians(72 * k)), cy + R * math.sin(math.radians(72 * k))) for k in range(5)]
line(ax, P + [P[0]], 'fixe', lw=0.6)
for k, (x, y) in enumerate(P):
    disc(ax, x, y, 1.4, 'sujet' if k == 1 else 'fixe')
text(ax, P[1][0] - 1, P[1][1] + 4, r'$\zeta$', 'sujet', 'm')
text(ax, P[0][0] + 4, P[0][1], r'$1$', 'fixe', 's')
text(ax, 64, 64, 'sommet du pentagone', 'fixe', 's')
text(ax, 64, 15, r'annule $\Phi_5$, de degré 4', 'sujet', 's')
text(ax, 64, 8, r'$x^4+x^3+x^2+x+1$', 'sujet', 's')
save(fig, '66-079')
