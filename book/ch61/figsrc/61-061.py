import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 22, 48, 44, 12, 'sujet', label=r'$f(x)=x^2-2$', size='l')
arrow(ax, (34, 47.5), (22, 36)); arrow(ax, (54, 47.5), (66, 36))
text(ax, 17, 42, r'$x\to 3$', 'varie', 's'); text(ax, 72, 42, r'$x\to\sqrt{2}$', 'varie', 's')
box(ax, 4, 24, 36, 11, 'fixe', label=r'$f(3)=9-2$', size='m'); box(ax, 48, 24, 36, 11, 'resultat', label=r'$f(\sqrt{2})=0$', size='m')
text(ax, 22, 14, 'le résultat : 7', 'fixe', 's'); text(ax, 66, 14, '$\\sqrt{2}$ est une racine', 'resultat', 's')
text(ax, 44, 5, 'on remplace $x$, on calcule', 'varie', 's')
save(fig, '61-061')
