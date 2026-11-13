import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, "l'horloge à six heures", 'fixe', 's')
# left: the element
disc(ax, 20, 26, 7, 'sujet', label=r'$e$', size='l')
text(ax, 20, 12, 'un élément', 'sujet', 'm')
text(ax, 20, 6, "l'heure 0", 'fixe', 's')
text(ax, 44, 26, r'$\neq$', 'limite', 'xl')
# right: the collection
box(ax, 54, 17, 28, 18, 'resultat', dash=True)
disc(ax, 68, 26, 7, 'sujet', label=r'$e$', size='l')
text(ax, 58, 38, r'$\{$', 'resultat', 'l'); text(ax, 78, 38, r'$\}$', 'resultat', 'l')
text(ax, 68, 12, 'une collection', 'resultat', 'm')
text(ax, 68, 6, r'$\{e\}$ : le neutre seul', 'resultat', 's')
save(fig, '45-209')
