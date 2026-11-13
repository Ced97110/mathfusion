import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(60)
text(ax, 20, 55, 'pente', 'autre', 'm')
text(ax, 66, 55, 'dérivée formelle', 'sujet', 'm')
xs = np.linspace(4, 36, 60)
ys = 14 + 18 * ((xs - 4) / 32) ** 2
ax.plot(xs, ys, color=COL['autre'], lw=1.2, zorder=3)
line(ax, [(11, 18.5 + 0.5625 * (11 - 20)), (29, 18.5 + 0.5625 * (29 - 20))], 'autre', dash=True)
text(ax, 20, 8, 'limite, nombres réels', 'autre', 's')
box(ax, 44, 34, 42, 12, 'sujet', label=r'$a_2x^2\to 2a_2x$', size='s')
box(ax, 44, 18, 42, 12, 'sujet', label=r'$a_3x^3\to 3a_3x^2$', size='s')
text(ax, 65, 8, 'règle sur les coefficients', 'sujet', 's')
text(ax, 65, 49.5, 'dans tout corps', 'sujet', 's')
save(fig, '62-090')
