import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
gy = 8
line(ax, [(2, gy), (86, gy)], 'fixe')
poly(ax, [(46, gy), (68, 38), (86, gy)], 'fixe')
disc(ax, 68, 38, 1.6, 'sujet')
text(ax, 18, 30, '$S$', 'sujet', 'xl')
text(ax, 18, 20, 'se lit « S »', 'sujet', 's')
arrow(ax, (27, 34), (65.5, 38), 'varie', curve=-0.15)
text(ax, 40, 44, 'le sommet : un point', 'sujet', 's')
text(ax, 66, 18, 'pas une longueur', 'fixe', 's')
save(fig, '38-010')
