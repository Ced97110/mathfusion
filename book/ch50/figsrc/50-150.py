import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 62, r'$e$ commun aux six 5-Sylow', 'fixe', 's')
disc(ax, 44, 55, 2.6, 'fixe')
for c in range(6):
    x = 9 + c * 14
    box(ax, x - 5.5, 17, 11, 29, 'sujet', fill=True)
    line(ax, [(44, 52.4), (x, 46)], 'fixe')
    for k in range(4):
        disc(ax, x, 21.5 + k * 6.5, 2.1, 'resultat')
text(ax, 44, 11, r'$6 \times 4 = 24$ éléments d’ordre 5', 'resultat', 'm', weight='bold')
text(ax, 44, 5, '4 par sous-groupe, aucun en double', 'fixe', 's')
save(fig, '50-150')
