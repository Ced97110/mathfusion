import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(62)
xs = np.linspace(0, 2 * math.pi, 200)
def panel(x0, role2, dash2, f2, cross):
    w, h, y0 = 36, 28, 18
    arrow(ax, (x0, y0 + h / 2), (x0 + w + 2, y0 + h / 2), 'fixe', lw=0.7)
    line(ax, [(x0, y0), (x0, y0 + h)], 'fixe', lw=0.7)
    X = x0 + xs / (2 * math.pi) * w
    ax.plot(X, y0 + h / 2 + np.sin(xs) * 11, color=COL['sujet'], lw=2.4, zorder=3)
    ax.plot(X, y0 + h / 2 + f2(xs) * 11, color=COL[role2], lw=1.0, ls='--' if dash2 else '-', zorder=4)
    for c in cross:
        disc(ax, x0 + c / (2 * math.pi) * w, y0 + h / 2 + math.sin(c) * 11, 1.3, 'encre')
panel(4, 'encre', True, np.sin, [])
panel(48, 'varie', False, lambda x: 0.5 + 0 * x, [math.asin(0.5), math.pi - math.asin(0.5)])
text(ax, 22, 12, 'courbes confondues', 'sujet', 'm')
text(ax, 22, 5.5, 'on soupçonne une identité', 'sujet', 's')
text(ax, 66, 12, 'courbes qui se croisent', 'varie', 'm')
text(ax, 66, 5.5, 'on a une équation', 'varie', 's')
text(ax, 66, 54, 'points communs', 'encre', 's')
text(ax, 22, 54, 'toute la courbe commune', 'encre', 's')
save(fig, '31-086')
