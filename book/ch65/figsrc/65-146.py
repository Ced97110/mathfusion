import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 2, 4, 84, 76, 'fixe', fill=True, label=None)
text(ax, 44, 74, 'tous les groupes finis', 'fixe', 'm')
box(ax, 7, 46, 36, 20, 'resultat', label=r'$S_n$ et $A_n$' + '\n' + 'oui, tout $n$', size='s')
box(ax, 47, 46, 36, 20, 'resultat', label='groupes résolubles\noui', size='s')
text(ax, 65, 41, 'Šafarevič, 1954', 'resultat', 's')
box(ax, 7, 9, 76, 22, 'fixe', fill=False, dash=True, label='cas général : ouvert', size='m')
save(fig, '65-146')
