import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
L = r'$\cos^4\varphi-\sin^4\varphi$'; Rr = r'$\cos 2\varphi$'
text(ax, 44, 76, 'Méthode 1 : transformer un membre', 'varie', 's')
box(ax, 2, 56, 38, 13, 'sujet', label=L, size='s')
arrow(ax, (40.5, 62.5), (51, 62.5), 'varie')
box(ax, 51.5, 56, 34, 13, 'autre', label=Rr, size='m')
text(ax, 45.75, 67.5, '', 'varie')
text(ax, 44, 42, 'Méthode 2 : calculer la différence', 'varie', 's')
box(ax, 2, 22, 52, 13, 'sujet', label=r'$\cos^4\varphi-\sin^4\varphi-\cos 2\varphi$', size='s')
arrow(ax, (54.5, 28.5), (62, 28.5), 'varie')
box(ax, 62.5, 22, 23, 13, 'resultat', label=r'$0$', size='l')
box(ax, 14, 3, 60, 11, 'resultat', label=r'avec des lettres : tout angle $\varphi$', size='s')
save(fig, '34-143')
