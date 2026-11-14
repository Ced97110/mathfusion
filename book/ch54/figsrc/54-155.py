import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$x^2$ divisé par $2x-1$ dans $\mathbb{Z}[x]$', 'sujet', 'm')
# sans facteur
box(ax, 3, 28, 39, 38, 'limite')
text(ax, 22.5, 61, 'sans le facteur', 'limite', 's')
text(ax, 22.5, 52, r'$x^2-\frac{1}{2}x\cdot g$', 'limite', 'm')
text(ax, 22.5, 42, r'coefficient $\frac{1}{2}$', 'limite', 's')
text(ax, 22.5, 34, 'pas un entier', 'limite', 's')
# avec facteur
box(ax, 46, 28, 39, 38, 'resultat')
text(ax, 65.5, 61, 'avec le facteur', 'resultat', 's')
text(ax, 65.5, 52, r'$2x^2-x\cdot g=x$', 'resultat', 'm')
text(ax, 65.5, 42, r'on a multiplié par 2', 'varie', 's')
text(ax, 65.5, 34, 'tout reste entier', 'resultat', 's')
text(ax, 44, 14, r'$2\,x^2$ au lieu de $x^2$ : étape permise', 'encre', 's')
save(fig, '54-155')
