import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
u = 28
S3 = math.sqrt(3)
x0, y0 = 30, 11
zx, zy = x0 + u / 2, y0 + S3 * u / 2
corners = [(x0, y0), (x0 + u, y0), (x0 + u, y0 + S3 * u), (x0, y0 + S3 * u)]
disc(ax, zx, zy, u, 'fixe', fill=False, lw=0.8)
poly(ax, corners, 'sujet', fill=False, lw=1.0)
for p in corners:
    line(ax, [(zx, zy), p], 'varie', lw=0.7, dash=True)
    disc(ax, p[0], p[1], 1.4, 'sujet')
disc(ax, zx, zy, 1.4, 'varie')
text(ax, zx + 4, zy - 3, r'$z$', 'varie', 'm')
text(ax, x0 - 3, y0 - 3, r'$0$', 'sujet', 'm')
text(ax, x0 + u + 3, y0 - 3, r'$1$', 'sujet', 'm')
text(ax, x0 - 3, y0 + S3 * u + 3, r'$\sqrt{3}\,i$', 'sujet', 'm', ha='right')
text(ax, x0 + u + 3, y0 + S3 * u + 3, r'$1+\sqrt{3}\,i$', 'sujet', 'm', ha='left')
text(ax, 72, 40, 'rayon 1', 'fixe', 's')
save(fig, '56-199')
