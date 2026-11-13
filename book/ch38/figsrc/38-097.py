import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(96)
# courbe y = 10 / x pour x de 0,055 à 1 ; x : 70 mm par unité ; y : 0,3 mm par unité
o = (8.0, 30.0)
kx, ky = 70.0, 0.3
xs = [0.055 + (1 - 0.055) * i / 300 for i in range(301)]
line(ax, [(o[0] + kx * x, o[1] + ky * 10 / x) for x in xs], 'sujet', lw=1.4)
arrow(ax, o, (o[0] + 78, o[1]), 'fixe', lw=0.8)
text(ax, 84, o[1] - 3, r'$x$', 'fixe', 's')
text(ax, 44, 91, r'$10\div x$ : où $x$ est petit', 'encre', 'm')
for x, y0, role in ((0.05669, 10 / 0.05669, 'varie'), (0.05844, 10 / 0.05844, 'varie'),
                    (0.86603, 10 / 0.86603, 'resultat'), (0.86690, 10 / 0.86690, 'resultat')):
    disc(ax, o[0] + kx * x, o[1] + ky * y0, 1.0, role)
text(ax, 24, 84, '176,4 et 171,1', 'varie', 's', ha='left')
text(ax, 24, 80, 'écart 5,3', 'varie', 's', ha='left')
text(ax, 54, 46, '11,547 et 11,535', 'resultat', 's', ha='left')
text(ax, 54, 42, 'écart 0,012', 'resultat', 's', ha='left')
text(ax, o[0] + kx * 0.057, o[1] - 3, '0,057', 'varie', 's')
text(ax, o[0] + kx * 0.866, o[1] - 3, '0,87', 'resultat', 's')
# trois domaines où le danger se présente
text(ax, 44, 21.5, 'même danger dans les trois cas', 'varie', 's', weight='bold')
for bx, lab in ((4, 'fractions'), (32, 'droites presque\nparallèles'), (60, 'déterminant\npresque nul')):
    box(ax, bx, 3, 24, 11, 'varie', label=lab, size='s')
    arrow(ax, (bx + 12, 19), (bx + 12, 14.6), 'varie', lw=1.0)
save(fig, '38-097')
