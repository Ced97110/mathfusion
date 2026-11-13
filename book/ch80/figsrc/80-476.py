import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(88)
text(ax, 44, 83, 'point de l\'espace', 'encre', 'm')
for j, v in enumerate(['2', '3', '5']):
    box(ax, 12 + j * 16, 62, 13, 11, 'sujet', label=v)
arrow(ax, (31, 59), (31, 51), 'varie'); text(ax, 52, 55, 'on ajoute 1', 'varie', 's')
for j, v in enumerate(['2', '3', '5', '1']):
    box(ax, 12 + j * 16, 38, 13, 11, 'varie' if j == 3 else 'sujet', label=v)
arrow(ax, (31, 35), (31, 27), 'varie'); text(ax, 36, 31, 'perspective : linéaire', 'varie', 's', ha='left')
for j, v in enumerate([r"$x'$", r"$y'$", r"$z'$", r"$w'$"]):
    box(ax, 12 + j * 16, 14, 13, 11, 'resultat', label=v)
save(fig, '80-476')
