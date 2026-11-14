import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
sea = 12
# relief : un plateau haut, une descente, un bord de mer bas
poly(ax, [(4, sea), (4, 46), (34, 46), (50, 24), (84, 24), (84, sea)], 'fixe')
line(ax, [(4, sea), (84, sea)], 'sujet', lw=1.0, dash=True)
text(ax, 44, sea - 4, 'niveau de la mer', 'sujet', 's')
# deux bases mesurées au sol, à deux altitudes
line(ax, [(8, 46), (30, 46)], 'varie', lw=2.4)
line(ax, [(56, 24), (78, 24)], 'varie', lw=2.4)
text(ax, 19, 51, 'base sur le plateau', 'varie', 's')
text(ax, 67, 29, 'base au bord de la mer', 'varie', 's')
# mêmes bases ramenées au niveau de la mer
for x0, x1 in ((8, 30), (56, 78)):
    for x in (x0, x1):
        ax.plot([x, x], [sea + 0.8, (46 if x0 == 8 else 24) - 0.8], color=COL['varie'], lw=0.8, ls='--', zorder=3)
    line(ax, [(x0, sea), (x1, sea)], 'resultat', lw=2.4)
text(ax, 19, 21, 'ramenée', 'resultat', 's')
text(ax, 67, 17.5, 'ramenée', 'resultat', 's')
text(ax, 44, 63, 'toutes les mesures ramenées au niveau de la mer', 'encre', 's')
save(fig, '38-091')
