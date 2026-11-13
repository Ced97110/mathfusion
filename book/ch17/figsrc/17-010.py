import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'inéquation = un outil pour 3 tâches', 'sujet', 's')
for y, lab in [(52, 'écrire'), (32, 'dessiner'), (12, 'calculer')]:
    box(ax, 4, y, 24, 14, 'sujet', label=lab, size='m')
    arrow(ax, (29, y + 7), (36, y + 7), 'fixe')
box(ax, 37, 52, 47, 14, 'fixe', label=r'$3 + 2d \leq 15$', size='l')
f = numberline(ax, 42, 66, 39, 0, 7, labels=False, arrow_right=True)
line(ax, [(f(0), 39), (f(6), 39)], 'resultat', lw=2.4)
disc(ax, f(0), 39, 1.6, 'resultat'); disc(ax, f(6), 39, 1.6, 'resultat')
text(ax, f(0), 33.5, '0', 'resultat', 's'); text(ax, f(6), 33.5, '6', 'resultat', 's')
box(ax, 37, 12, 47, 14, 'resultat', label='de 0 à 6 km', size='l')
save(fig, '17-010')
