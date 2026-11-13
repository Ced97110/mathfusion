import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(60)
x0, y0, sx, sy = 10, 10, 70 / 10, 0.8
X = lambda t: x0 + t * sx
Y = lambda h: y0 + h * sy
arrow(ax, (X(0), Y(0)), (X(10) + 4, Y(0)), 'fixe', lw=0.7)
line(ax, [(X(0), Y(0)), (X(0), Y(47))], 'fixe', lw=0.7)
line(ax, [(X(0), Y(22)), (X(10), Y(22))], 'fixe', dash=True)
t = np.linspace(0, 10, 300)
line(ax, list(zip(X(t), Y(20 * np.sin(np.pi / 4 * (t - 2)) + 22))), 'sujet', lw=1.3)
for tv, hv in ((0, 2), (4, 42)):
    disc(ax, X(tv), Y(hv), 1.5, 'resultat')
    line(ax, [(X(tv), Y(hv)), (X(tv), Y(0))], 'resultat', lw=0.5, dash=True)
text(ax, X(0), y0 - 3.2, '0', 'resultat', 's')
text(ax, X(4), y0 - 3.2, '4', 'resultat', 's')
text(ax, X(1.4), Y(3.5), r'$t=0:\ -20+22=2$', 'resultat', 's', ha='left')
text(ax, X(4) + 3, Y(42) + 2.5, r'$t=4:\ 20+22=42$', 'resultat', 's', ha='left')
text(ax, X(10), Y(22) + 3, 'ligne médiane', 'fixe', 's', ha='right')
save(fig, '30-135')
