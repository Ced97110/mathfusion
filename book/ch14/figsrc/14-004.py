import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
c, g = 3.4, 0.4
def row(n, y, role):
    for i in range(n): box(ax, 2.4 + i * (c + g), y, c, c, role, r=0.4)
row(22, 58, 'sujet'); row(21, 46, 'autre')
text(ax, 2.5, 65, r'$2^{72}$ : 22 chiffres', 'sujet', 'm', ha='left')
text(ax, 2.5, 53, '21 chiffres', 'autre', 'm', ha='left')
text(ax, 86, 53, 'presque pareils', 'fixe', 's', ha='right')
text(ax, 44, 38.5, 'pour la taille : compter les cases', 'fixe', 's')
arrow(ax, (44, 35), (44, 27), 'resultat', lw=1.2)
box(ax, 14, 4, 60, 22, 'resultat')
text(ax, 44, 19, r'$10^{21}$', 'resultat', 'xl')
text(ax, 44, 12.5, '21 facteurs 10', 'resultat', 's')
text(ax, 44, 7.8, 'la taille se lit d’un coup', 'resultat', 's')
save(fig, '14-004')
