import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
disc(ax, 44, 38, 30, 'resultat')
disc(ax, 30, 38, 11, 'sujet')
text(ax, 30, 38, '$F$', 'sujet', 'xl')
text(ax, 30, 49.8, 'départ', 'sujet', 's')
for (x, y), nm in zip([(52, 50), (62, 38), (52, 26)], ['$r_1$', '$r_2$', '$r_3$']):
    disc(ax, x, y, 1.6, 'varie')
    text(ax, x + 4.5, y, nm, 'varie', 'm')
text(ax, 44, 58, '$E$ : le plus petit corps', 'resultat', 'm')
text(ax, 44, 3, '$f$ s’y casse en facteurs de degré 1', 'encre', 'm')
save(fig, '62-009')
