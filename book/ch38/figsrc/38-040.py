import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
g = 10.0
# Gauche : le segment SH (hauteur) sur le sol
xh = 18.0
line(ax, [(4, g), (34, g)], 'fixe')
arrow(ax, (xh, g + 1), (xh, g + 38), 'resultat', lw=1.6, both=True)
disc(ax, xh, g, 1.2, 'resultat'); disc(ax, xh, g + 39.5, 1.2, 'resultat')
text(ax, xh, g - 3.5, 'H', 'resultat', 's')
text(ax, xh, g + 44, 'S', 'resultat', 's')
text(ax, xh + 3, g + 19.5, 'h = SH', 'resultat', 'm', ha='left', weight='bold')
# Droite : trois nombres mesurés donnent h
for i, lab in enumerate(['d = 1 000 m', 'α = 18°', 'β = 21,25°']):
    y = 46 - i * 11
    box(ax, 52, y, 34, 9, 'fixe', label=lab, size='s')
box(ax, 40, 5, 46, 9, 'resultat', label='h ≈ 1 976 m', size='m', weight='bold')
text(ax, 69, 58, 'mesurés', 'fixe', 's')
text(ax, 56, 19, 'calculée', 'resultat', 's', ha='right')
arrow(ax, (69, 22.5), (69, 15.5), 'varie')
save(fig, '38-040')
