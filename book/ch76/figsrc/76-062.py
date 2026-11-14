import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 56, 'Jacobson', 'autre', 's'); text(ax, 66, 56, 'la plupart des livres', 'sujet', 's')
box(ax, 2, 24, 36, 26, 'autre'); box(ax, 50, 24, 36, 26, 'sujet')
text(ax, 20, 43, r'$E(V)$', 'autre', 'l'); text(ax, 68, 43, r'$\Lambda(V)$', 'sujet', 'l')
text(ax, 20, 31, r'$e_1e_2$', 'autre', 'l'); text(ax, 68, 31, r'$e_1\wedge e_2$', 'sujet', 'l')
text(ax, 44, 37, '=', 'resultat', 'xl')
text(ax, 44, 52, 'même algèbre', 'resultat', 's') if False else None
text(ax, 20, 17, 'sans symbole', 'autre', 's')
arrow(ax, (72, 17), (72, 26), 'varie') if False else None
arrow(ax, (72, 14), (72, 25), 'varie')
text(ax, 68, 8, 'se lit « extérieur »', 'varie', 's')
text(ax, 44, 3, 'même algèbre, même produit', 'resultat', 's') if False else None
save(fig, '76-062')
