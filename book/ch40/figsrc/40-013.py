import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import pi, cos, sin, radians
fig, ax = canvas(56)
O = (40.0, 26.0); u = 16.0  # 1 cm = 16 mm
arrow(ax, (O[0] - 36, O[1]), (O[0] + 44, O[1]), 'fixe', lw=1.0, both=True)
text(ax, 3, O[1] + 5, 'axe des $x$', 'fixe', 's', ha='left')
text(ax, 3, O[1] - 5, '(droite entière)', 'fixe', 's', ha='left')
arrow(ax, O, (O[0] + 44, O[1]), 'sujet', lw=2.2)
disc(ax, *O, 1.4, 'encre')
text(ax, O[0], O[1] - 5, 'pôle $O$', 'encre', 's')
text(ax, O[0] + 22, O[1] + 6, 'axe polaire', 'sujet', 'm')
text(ax, O[0] + 22, O[1] - 9, '(demi-droite)', 'sujet', 's')
disc(ax, O[0] + 2 * u, O[1], 1.3, 'resultat')
text(ax, O[0] + 2 * u, O[1] + 12, '2 cm :\nangle 0', 'resultat', 's')
line(ax, [(O[0] + 2 * u, O[1] + 3), (O[0] + 2 * u, O[1] + 9)], 'resultat', lw=0.5)
# angle : mesuré depuis l'axe polaire, sens inverse des aiguilles
arrow(ax, (O[0] + 9, O[1] + 1.5), (O[0] + 5, O[1] + 8.5), 'varie', curve=0.5)
text(ax, O[0] + 2, O[1] + 13, r'$\theta$ part d’ici', 'varie', 's')
save(fig, '40-013')
