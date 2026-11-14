import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(62)
sy = 5.0
cy = 28.0
def panel(ox, sx, xmin, xmax, f, roots, title, labs):
    line(ax, [(ox + xmin * sx, cy), (ox + xmax * sx, cy)], 'fixe', lw=0.6)
    xs = np.linspace(xmin, xmax, 80)
    ax.plot(ox + xs * sx, cy + f(xs) * sy, color=COL['varie'], lw=1.2, zorder=3)
    text(ax, ox, 54, title, 'varie', 's')
    for r, lab, role, dy in zip(roots, labs, ['sujet', 'fixe'], [-7, -7]):
        disc(ax, ox + r * sx, cy, 1.5, role)
        text(ax, ox + r * sx, cy + dy, lab, role, 's')
panel(20, 12.0, -0.6, 1.6, lambda x: 2 * x - 1, [0.5], r'$f(x)=2x-1$', [r'$u=\frac{1}{2}$'])
panel(65, 9.0, -2.0, 2.0, lambda x: x ** 2 - 2, [2 ** 0.5, -2 ** 0.5], r'$f(x)=x^2-2$', [r'$u=\sqrt{2}$', r'$-\sqrt{2}$'])
text(ax, 20, 12, r'$f(u)=0$', 'sujet', 'm')
text(ax, 65, 12, r'$f(u)=0$', 'sujet', 'm')
text(ax, 44, 4, 'un polynôme non nul s’annule en $u$', 'encre', 's')
save(fig, '66-073')
