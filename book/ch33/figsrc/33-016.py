import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(74)
k = 70 / 270; amp = 9
X = lambda d: 8 + (d + 90) * k
panels = [(54, -90, 90, 'sujet', 'bande −90° à 90° : 1 point', [(30, 'A', 'resultat')]),
          (20, 0, 180, 'autre', 'bande 0° à 180° : 2 points', [(30, 'A', 'resultat'), (150, 'B', 'limite')])]
for y0, a, b, r, title, pts in panels:
    ax.add_patch(Rectangle((X(a), y0 - amp - 3), (b - a) * k, 2 * amp + 6, fc=FILL[r], ec=COL[r], lw=0.6, zorder=1))
    d = np.linspace(a, b, 200)
    ax.plot(X(d), y0 + amp * np.sin(np.radians(d)), color=COL['encre'], lw=1.1, zorder=3)
    line(ax, [(X(a), y0 + amp / 2), (X(b), y0 + amp / 2)], 'varie', lw=1.0)
    for dd, nm, rr in pts:
        disc(ax, X(dd), y0 + amp / 2, 1.2, rr)
        text(ax, X(dd), y0 + amp / 2 + 4.3, r'$' + nm + '$', rr, 'm')
    text(ax, X(a), y0 - amp - 6, f'{a}°'.replace('-', '−'), r, 's')
    text(ax, X(b), y0 - amp - 6, f'{b}°', r, 's')
    text(ax, (X(a) + X(b)) / 2, y0 + amp + 6.5, title, r, 's')
save(fig, '33-016')
