import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(58)
x0, x1 = 8, 78; y0, amp = 26, 20
X = lambda d: x0 + d / 180 * (x1 - x0)
t = np.linspace(0, math.pi, 200)
ax.plot(x0 + t / math.pi * (x1 - x0), y0 + amp * np.sin(t), color=COL['encre'], lw=1.1, zorder=3)
line(ax, [(x0 - 2, y0), (x1 + 2, y0)], 'fixe')
line(ax, [(x0, y0 + amp / 2), (x1, y0 + amp / 2)], 'varie', lw=1.0, dash=True)
for d, nm in ((30, 'A'), (150, 'B')):
    disc(ax, X(d), y0 + amp / 2, 1.3, 'sujet')
    text(ax, X(d), y0 + amp / 2 + 4, r'$' + nm + '$', 'sujet', 'l')
    line(ax, [(X(d), y0), (X(d), y0 + amp / 2)], 'sujet', lw=0.6, dash=True)
text(ax, X(90), y0 + amp / 2 - 3.5, 'même hauteur', 'varie', 's')
for d in (0, 180):
    text(ax, X(d), y0 + 3.5, '0' if d == 0 else r'$\pi$', 'fixe', 's')
brace(ax, X(0), X(30), y0 - 3, 'sujet', label=r'$\pi/6$')
brace(ax, X(150), X(180), y0 - 3, 'sujet', label=r'$\pi/6$')
brace(ax, X(0), X(150), y0 - 12, 'resultat', label=r'$5\pi/6 = \pi - \pi/6$')
save(fig, '33-013')
