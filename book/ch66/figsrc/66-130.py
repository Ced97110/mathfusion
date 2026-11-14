import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(62)
text(ax, 44, 57, r'$h=x^{2}(x-2)^{3}$, $p=3$', 'encre', 'm')
axis_y = 24
X = lambda v: 4 + (v - 1.4) / 1.2 * 40
xs = np.linspace(1.4, 2.6, 60)
ys = axis_y + 14 * xs ** 2 * (xs - 2) ** 3
line(ax, [(4, axis_y), (46, axis_y)], 'fixe')
line(ax, list(zip(X(xs), ys)), 'sujet', lw=1.2)
disc(ax, X(2), axis_y, 1.3, 'varie')
text(ax, X(2), 14, r'$u_i=2$', 'varie', 's')
text(ax, 15, 46, r'courbe de $h$', 'sujet', 's')
for i, s in enumerate([r'$h(2)=0$', r"$h'(2)=0$", r"$h''(2)=0$"]):
    box(ax, 54, 42 - i * 12, 32, 9, 'resultat', label=s)
text(ax, 70, 11, '3 valeurs nulles de suite', 'resultat', 's')
save(fig, '66-130')
