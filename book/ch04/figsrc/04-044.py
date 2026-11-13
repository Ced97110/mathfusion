import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(80)

# séparation entre les deux sortes de règles
line(ax, [(44, 20), (44, 78)], 'fixe', lw=0.5)

# colonne gauche : une règle démontrée
text(ax, 22, 74, 'règle démontrée', 'resultat', 'm')
text(ax, 22, 68, 'se prouve : on peut vérifier', 'resultat', 's')
for i in range(4):
    for j in range(4):
        box(ax, 12 + i * 5, 34 + j * 5, 4.6, 4.6, 'resultat', r=0.4)
text(ax, 22, 27, '4 × 4 = 16 : on compte 16', 'resultat', 's')

# colonne droite : une convention, un accord
text(ax, 66, 74, 'convention', 'sujet', 'm')
text(ax, 66, 68, 'se connaît, ne se prouve pas', 'sujet', 's')
text(ax, 52.6, 52.6, '2', 'varie', 'xl', weight='bold')
text(ax, 57, 48, '√16', 'sujet', 'l')
arrow(ax, (63, 48), (71, 48), 'varie', lw=1.0)
text(ax, 78, 48, '√16', 'sujet', 'l')
text(ax, 67, 42, 'le 2 n’est pas écrit', 'varie', 's')
text(ax, 66, 27, 'accord entre ceux qui écrivent', 'sujet', 's')

# ligne du bas : la limite
text(ax, 44, 10, 'sans l’accord : pas compris', 'limite', 's')

save(fig, '04-044')
