import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
c = 9
def row(y, vals, role, third):
    for j, v in enumerate(vals):
        box(ax, 8 + j * c, y, c, c, third if j == 2 else role, label=str(v))
row(48, [1, 2, 3], 'sujet', 'sujet')
row(26, [1, 2, 4], 'sujet', 'varie')
text(ax, 8 + 1.5 * c, 61, r'$x$', 'sujet', 'l')
text(ax, 8 + 1.5 * c, 39, r'$x + r$', 'sujet', 'l')
box(ax, 54, 31, 28, 12, 'resultat', label=r'$-7$', size='l')
arrow(ax, (8 + 3 * c + 2, 52), (53, 40), 'resultat')
arrow(ax, (8 + 3 * c + 2, 30), (53, 34), 'resultat')
text(ax, 68, 48, 'même mesure', 'resultat', 's')
text(ax, 68, 25, r'avec $y = (5, 6, 7)$', 'fixe', 's')
text(ax, 8 + 3.5 * c, 19, '3e nombre : jamais lu', 'varie', 's', ha='center')
text(ax, 44, 8, 'deux vecteurs, une seule mesure', 'encre', 's')
save(fig, '72-034')
