import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
x0, y0, L = 6, 14, 74   # horizontal run 100 m -> L mm
rise = L * 10 / 100
line(ax, [(x0 - 4, y0), (x0 + L + 4, y0)], 'fixe', lw=1.0)
line(ax, [(x0, y0), (x0 + L, y0 + rise)], 'sujet', lw=1.6)
line(ax, [(x0 + L, y0), (x0 + L, y0 + rise)], 'fixe', dash=True)
import math
th = math.atan2(rise, L)
r = 24
pts = [(x0 + r * math.cos(t), y0 + r * math.sin(t)) for t in [th * i / 20 for i in range(21)]]
line(ax, pts, 'varie', lw=1.2)
arrow(ax, (x0 + 22, y0 + 9), (x0 + r - 1, y0 + 1.6), 'varie')
text(ax, x0 + 22, y0 + 12.5, 'θ ≈ 5,71°', 'varie', 'm')
text(ax, x0 + 52, y0 + 14, 'chemin', 'sujet', 'm', weight='bold')
text(ax, x0 + 30, y0 - 4, 'horizontale', 'fixe', 's')
text(ax, x0 + L - 2, y0 + rise / 2 - 6.5 + 6, '10 m', 'fixe', 's', ha='right') if False else None
text(ax, x0 + 52, y0 - 4, '100 m', 'fixe', 's')
text(ax, x0 + L + 1, y0 + rise / 2, '10 m', 'fixe', 's', ha='left')
save(fig, '26-085')
