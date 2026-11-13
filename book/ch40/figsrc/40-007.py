import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# haut : le grand axe entier, de 0 à 299,3
x0, x1, y = 6.0, 82.0, 68.0
F = lambda v: x0 + v / 299.3 * (x1 - x0)
line(ax, [(x0, y), (x1, y)], 'fixe', lw=1.0)
for v in (0, 299.3):
    line(ax, [(F(v), y - 1.5), (F(v), y + 1.5)], 'fixe')
text(ax, x0 + 2, y + 6, 'plus près', 'resultat', 's')
text(ax, x1 - 2, y + 6, 'plus loin', 'resultat', 's')
brace(ax, x0, x1, y + 2.5, 'fixe', label='grand axe : 299,3', down=False)
for v in (147.1, 149.65, 152.2):
    disc(ax, F(v), y, 0.7, 'sujet')
# fenêtre agrandie entre 146 et 153
Z0, Z1, zy = 8.0, 80.0, 30.0
f = numberline(ax, Z0, Z1, zy, 146, 153, step=1, arrow_right=False, role='fixe')
line(ax, [(F(147.1), y - 1), (Z0, zy + 8)], 'fixe', lw=0.4, dash=True)
line(ax, [(F(152.2), y - 1), (Z1, zy + 8)], 'fixe', lw=0.4, dash=True)
text(ax, 44, 52, 'agrandissement', 'fixe', 's')
disc(ax, f(147.1), zy, 1.5, 'sujet')
disc(ax, f(149.65), zy, 1.5, 'fixe')
disc(ax, f(152.2), zy, 1.5, 'autre')
text(ax, f(147.1), zy + 5, 'Soleil', 'sujet', 's')
text(ax, f(149.65), zy + 5, 'centre', 'fixe', 's')
text(ax, f(152.2), zy + 5, '2e foyer', 'autre', 's')
brace(ax, f(147.1), f(149.65), zy - 7, 'varie', label='2,55', size='s')
brace(ax, f(149.65), f(152.2), zy - 7, 'varie', label='2,55', size='s')
text(ax, 44, 4, '147,1 + 152,2 = 299,3', 'resultat', 'm')
save(fig, '40-007')
