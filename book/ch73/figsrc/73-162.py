import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
s = 0.08; ox, oy = 10, 10
X = lambda v: ox + v * s; Y = lambda v: oy + v * s
line(ax, [(ox, oy - 2), (X(800) + 4, oy - 2)], 'fixe')
line(ax, [(ox, oy), (ox, Y(200) + 4)], 'fixe', dash=True)
arrow(ax, (ox, Y(100) + 1.6), (ox, Y(200) - 1.6), 'varie')
arrow(ax, (X(0) + 1.6, Y(200)), (X(400) - 1.6, Y(200)), 'varie')
arrow(ax, (X(400) + 1.6, Y(200)), (X(800) - 1.6, Y(200)), 'varie')
disc(ax, ox, Y(100), 1.4, 'sujet'); disc(ax, ox, Y(200), 1.4, 'fixe')
disc(ax, X(400), Y(200), 1.4, 'fixe'); disc(ax, X(800), Y(200), 1.4, 'resultat')
text(ax, 15, Y(100), 'hauteur 100', 'sujet', 's', ha='left')
text(ax, 13.5, 22, 'hauteurs × 2', 'varie', 's', ha='left')
text(ax, 26, Y(200) + 5, 'glisse de 400', 'varie', 's')
text(ax, 58, Y(200) + 5, 'largeurs × 2', 'varie', 's')
text(ax, 58, Y(200) - 5, 'glissé de 800', 'resultat', 's')
text(ax, 44, 3, 'glissé 800 pour hauteur 100 : pente 8', 'encre', 's')
save(fig, '73-162')
