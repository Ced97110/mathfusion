import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ay, ly = 24, 38      # hauteur de l'axe (valeur 0) et de la droite f = 1
arrow(ax, (5, ay), (84, ay), 'fixe', lw=0.9)
line(ax, [(8, ly), (80, ly)], 'sujet', lw=1.6)
for x in (20, 36, 52):
    line(ax, [(x, ay), (x, ly)], 'fixe', dash=True)
    disc(ax, x, ly, 1.6, 'sujet')
text(ax, 20, ly + 5, r'$f=1$', 'sujet', 'm')
text(ax, 46, ay - 4, 'valeur 0', 'fixe', 's')
arrow(ax, (76, ay), (76, ly), 'limite', lw=1.0, both=True)
text(ax, 66, (ay + ly) / 2, 'jamais 0', 'limite', 's')
text(ax, 44, 11, 'aucune racine,', 'limite', 's')
text(ax, 44, 7, 'dans aucun corps', 'limite', 's')
save(fig, '62-154')
