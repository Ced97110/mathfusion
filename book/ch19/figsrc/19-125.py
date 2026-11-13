import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, ux, uy, x0, x1, y0, y1):
    arrow(ax, (ox + x0 * ux, oy), (ox + x1 * ux + 3, oy), "fixe", lw=0.8)
    arrow(ax, (ox, oy + y0 * uy), (ox, oy + y1 * uy + 3), "fixe", lw=0.8)
    return lambda x, y: (ox + x * ux, oy + y * uy)
import numpy as np
fig, ax = canvas(72); P = plane(ax, 12, 8, 17, 5.6, 0, 4, 0, 10)
xs = np.linspace(0, 3.1, 60)
line(ax, [P(x, x * x) for x in xs], 'sujet', lw=1.6)
pts = [(0, 0), (1, 1), (2, 4), (3, 9)]
for (x, y) in pts:
    disc(ax, *P(x, y), 1.2, 'sujet')
    text(ax, P(x, y)[0] - 2.5, P(x, y)[1] + 2.5, str(y), 'sujet', 's', ha='right')
for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
    line(ax, [P(x0, y0), P(x1, y0)], 'varie', dash=True)
    arrow(ax, P(x1, y0), P(x1, y1 - 0.25), 'varie', lw=1.2)
    text(ax, P(x1, (y0 + y1) / 2)[0] + 2, P(x1, (y0 + y1) / 2)[1], f'+{y1 - y0}', 'varie', 'm', ha='left', weight='bold')
for (x, y) in pts:
    text(ax, P(x, 0)[0], P(x, 0)[1] - 3, str(x), 'fixe', 's')
text(ax, 18, 62, r'$y=x\times x$', 'sujet', 'm', weight='bold', ha='left')
save(fig, '19-125')
