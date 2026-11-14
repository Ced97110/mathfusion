import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def axes_xy(ax, ox, oy, u, xmax, ymin, ymax, tx=(), ty=()):
    arrow(ax, (ox - 1.0 * u, oy), (ox + xmax * u, oy), 'fixe', lw=0.8)
    arrow(ax, (ox, oy + ymin * u), (ox, oy + ymax * u), 'fixe', lw=0.8)
    text(ax, ox + xmax * u + 3, oy, r'$x$', 'fixe'); text(ax, ox, oy + ymax * u + 3, r'$y$', 'fixe')
    for t in tx:
        line(ax, [(ox + t * u, oy - 1), (ox + t * u, oy + 1)], 'fixe'); text(ax, ox + t * u, oy - 3.2, f'{t}'.replace('-', '\u2212'), 'fixe', 's')
    for t in ty:
        line(ax, [(ox - 1, oy + t * u), (ox + 1, oy + t * u)], 'fixe'); text(ax, ox - 3.4, oy + t * u, f'{t}'.replace('-', '\u2212'), 'fixe', 's')
def curve(ax, ox, oy, u, role, lw=1.2):
    for xs in (np.linspace(-1, 1.62, 80), np.linspace(2.38, 6, 80)):
        ax.plot(ox + xs * u, oy + u / (xs - 2), color=COL[role], lw=lw, zorder=3)
ox, oy, u = 14, 32, 9
fig, ax = canvas(70)
axes_xy(ax, ox, oy, u, 6.8, -3, 3, tx=(1, 3, 4), ty=(1, -1))
line(ax, [(ox + 2 * u, oy - 3.3 * u), (ox + 2 * u, oy + 3.3 * u)], 'limite', lw=1.1, dash=True)
curve(ax, ox, oy, u, 'sujet')
text(ax, ox + 2 * u, oy + 3.3 * u + 3, r'$x = 2$', 'limite', 's')
text(ax, 64, 54, r'$y=\frac{1}{x-2}$', 'sujet', 'm')
text(ax, 14, 2, 'morceau de gauche', 'sujet', 's'); text(ax, 56, 46, 'morceau de droite', 'sujet', 's')
save(fig, '21-012')
