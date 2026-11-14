import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
X0, S = 14.0, 5.5          # abscisse x=2 en X0, 5,5 mm par unité
Y0, T = 32.0, 1.45         # axe horizontal, mm par unité verticale
gx = lambda x: X0 + (x - 2) * S
gy = lambda y: Y0 + y * T
pts = [(gx(2 + 12 * i / 120), gy((2 + 12 * i / 120) ** 2 - 16 * (2 + 12 * i / 120) + 55)) for i in range(121)]
line(ax, pts, 'sujet', lw=1.3)
arrow(ax, (X0 - 6, Y0), (gx(14) + 5, Y0), 'fixe', lw=0.8)
text(ax, gx(14) + 3, Y0 - 3.2, r'$x$', 'fixe', 's')
for x, nom in ((5, r'$p = 5$'), (11, r'$q = 11$')):
    disc(ax, gx(x), Y0, 1.3, 'resultat')
    text(ax, gx(x), Y0 - 6, nom, 'resultat', 'm', weight='bold')
text(ax, gx(8), gy(17), r'$x^{2} - 16x + 55 = 0$', 'sujet', 'm')
text(ax, gx(8), gy(11), 'somme 16, produit 55', 'fixe', 's')
save(fig, '53-162')
