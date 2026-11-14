import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np

fig, ax = canvas(62)
y0, A = 33, 13
X = lambda deg: 8 + (deg + 30)/360*72
arrow(ax, (6, y0), (84, y0), 'fixe', lw=0.8)
text(ax, 85.5, y0 + 3, 'θ', 'fixe', 's')
for k in range(6):
    a0 = -30 + 60*k
    th = np.linspace(a0, a0 + 60, 120)
    ys = y0 + A*np.cos(3*np.radians(th))
    xs = X(th)
    role = 'sujet' if k % 2 == 0 else 'varie'
    ax.fill_between(xs, y0, ys, color=FILL[role], zorder=1)
    ax.plot(xs, ys, color=COL[role], lw=1.2, zorder=3)
    sgn = 1 if k % 2 == 0 else -1
    text(ax, X(a0 + 30), y0 + sgn*6.5, str(k + 1), role, 'm', weight='bold')
brace(ax, X(-30), X(30), y0 + A + 1.5, 'resultat', label='60° = π/3', down=False)
brace(ax, X(-30), X(330), y0 - A - 3, 'fixe', label='2π ÷ (π/3) = 6 = 2n', down=True)
text(ax, 66, 55, 'r = cos 3θ  (n = 3)', 'sujet', 's')
save(fig, '40-059')
