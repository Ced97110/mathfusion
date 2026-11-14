import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
u = 26
S3 = math.sqrt(3)
x0, y0 = 6, 8
zx, zy = x0 + u / 2, y0 + S3 * u / 2
corners = [(x0, y0), (x0 + u, y0), (x0 + u, y0 + S3 * u), (x0, y0 + S3 * u)]
poly(ax, corners, 'sujet', fill=False, lw=1.0)
for p in corners:
    disc(ax, p[0], p[1], 1.2, 'sujet')
    line(ax, [(zx, zy), p], 'fixe', lw=0.6, dash=True)
line(ax, [(x0, y0), (zx, y0)], 'sujet', lw=1.2)
line(ax, [(zx, y0), (zx, zy)], 'varie', lw=1.2)
line(ax, [(x0, y0), (zx, zy)], 'resultat', lw=1.4)
disc(ax, zx, zy, 1.3, 'varie')
text(ax, zx, zy + 4, r'$z$', 'varie', 'm')
text(ax, (x0 + zx) / 2, y0 - 3.5, r'$\frac{1}{2}$', 'sujet', 'm')
text(ax, zx + 3, (y0 + zy) / 2, r'$\frac{\sqrt{3}}{2}$', 'varie', 'm', ha='left')
text(ax, x0 + 4, y0 + 17, '1', 'resultat', 'm')
text(ax, 62, 62, 'distance de $z$ à $0$', 'resultat', 's')
text(ax, 62, 50, r'$(\frac{1}{2})^2=\frac{1}{4}$', 'sujet', 'm')
text(ax, 62, 38, r'$(\frac{\sqrt{3}}{2})^2=\frac{3}{4}$', 'varie', 'm')
text(ax, 62, 26, r'$\frac{1}{4}+\frac{3}{4}=1$', 'resultat', 'm')
text(ax, 62, 12, 'même calcul aux 4 coins', 'fixe', 's')
save(fig, '56-200')
