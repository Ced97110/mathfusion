import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(60)
k = 70 / (3.5 * math.pi); y0, amp = 28, 14
X = lambda t: 8 + (t + math.pi / 2) * k
ax.add_patch(Rectangle((X(-math.pi / 2), y0 - amp - 4), math.pi * k, 2 * amp + 8, fc=FILL['sujet'], ec=COL['sujet'], lw=0.6, zorder=1))
line(ax, [(X(-math.pi / 2), y0), (X(3 * math.pi) + 2, y0)], 'fixe')
t = np.linspace(-math.pi / 2, 3 * math.pi, 400)
ax.plot(X(t), y0 + amp * np.sin(t), color=COL['encre'], lw=1.1, zorder=3)
line(ax, [(X(-math.pi / 2), y0 + amp / 2), (X(3 * math.pi) + 2, y0 + amp / 2)], 'varie', lw=1.1)
for n, c in enumerate([math.pi / 6, 5 * math.pi / 6, 13 * math.pi / 6, 17 * math.pi / 6]):
    disc(ax, X(c), y0 + amp / 2, 1.1, 'resultat' if n == 0 else 'fixe')
text(ax, X(math.pi / 6) - 3.2, y0 + amp / 2 + 3.2, r'$A$', 'resultat')
text(ax, X(2.3 * math.pi) + 6, y0 + amp / 2 + 3.5, r'$y = 0{,}5$', 'varie')
text(ax, X(-math.pi / 2), y0 - amp - 7, r'$-\pi/2$', 'sujet', 's')
text(ax, X(math.pi / 2), y0 - amp - 7, r'$\pi/2$', 'sujet', 's')
text(ax, X(-math.pi / 2) + 2, y0 + amp + 7, 'bande : 1 seul point', 'sujet', 's', ha='left')
text(ax, X(2.2 * math.pi), y0 - amp - 2, 'courbe du sinus', 'encre', 's')
text(ax, X(2.2 * math.pi), y0 - amp - 8, '4 points sur le dessin', 'fixe', 's')
save(fig, '33-011')
