import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, 'les classes à gauche existent', 'resultat', 'm')
names = [r'$H$', r'$rH$', r'$r^2H$', r'$r^3H$']
for i in range(4):
    box(ax, 2.25 + i * 21.5, 41, 19, 9, 'resultat', label=names[i])
brace(ax, 2.25, 85.75, 41, 'resultat', label='4 classes de 2 éléments')
for i in range(4):
    for j in range(4):
        box(ax, 4 + i * 6.5, 4 + j * 6.5, 6, 6, 'limite', fill=False, dash=True, r=0.5)
text(ax, 60, 20, 'produit des classes :', 'limite', 's')
text(ax, 60, 15, 'aucune valeur', 'limite', 's')
save(fig, '47-181')
