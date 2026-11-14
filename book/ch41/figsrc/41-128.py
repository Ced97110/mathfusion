import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
x0, x1 = 10, 78
fs = lambda v: x0 + v / 300 * (x1 - x0)
fa = lambda a: x0 + a / 60 * (x1 - x0)
# vitesse
y = 38
text(ax, 44, 49, 'vitesse au sol (km/h)', 'fixe', 's')
line(ax, [(fs(80), y), (fs(280), y)], 'fixe', lw=3.5)
box(ax, fs(80) - 1, y - 2.5, 2, 5, 'fixe')
box(ax, fs(280) - 1, y - 2.5, 2, 5, 'fixe')
disc(ax, fs(245.8), y, 2.2, 'resultat')
text(ax, fs(245.8), y + 6, r'résultat $\approx 245{,}8$', 'resultat', 's')
text(ax, fs(80), y - 6, 'différence 80', 'fixe', 's')
text(ax, fs(280), y - 6, 'somme 280', 'fixe', 's')
# direction
y2 = 12
text(ax, 44, 25, 'direction (° depuis l’est)', 'fixe', 's')
line(ax, [(fa(0), y2), (fa(60), y2)], 'fixe', lw=3.5)
box(ax, fa(0) - 1, y2 - 2.5, 2, 5, 'sujet')
box(ax, fa(60) - 1, y2 - 2.5, 2, 5, 'varie')
disc(ax, fa(20.6), y2, 2.2, 'resultat')
text(ax, fa(20.6), y2 + 6, r'résultat $\approx 20{,}6°$', 'resultat', 's')
text(ax, fa(0), y2 - 6, 'avion 0°', 'sujet', 's')
text(ax, fa(60), y2 - 6, 'vent 60°', 'varie', 's')
save(fig, '41-128')
