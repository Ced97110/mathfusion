import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
# Partie 1 : le lien x.2 - 2.x = 0
box(ax, 4, 66, 20, 9, 'sujet', label=r'$x\cdot 2$')
box(ax, 34, 66, 20, 9, 'resultat', label=r'$2x$')
box(ax, 64, 66, 20, 9, 'sujet', label=r'$2\cdot x$')
arrow(ax, (24.8, 70.5), (33.2, 70.5), 'varie')
arrow(ax, (63.2, 70.5), (54.8, 70.5), 'varie')
text(ax, 44, 59, r'$x\cdot 2-2\cdot x=0$', 'resultat', 'l')
text(ax, 44, 53.5, 'un lien, sans diviser', 'fixe', 's')
line(ax, [(4, 49), (84, 49)], 'fixe', lw=0.5, dash=True)
# Partie 2 : aucun g seul n'engendre K
text(ax, 44, 43, r'$g$ divise 2 : quatre choix', 'encre', 'm')
for i, v in enumerate(['1', '−1', '2', '−2']):
    box(ax, 4 + i * 21, 27, 19, 9, 'limite', label=v)
brace(ax, 4, 44, 27, 'limite', label=r'$\notin K$')
brace(ax, 46, 86, 27, 'limite', label=r'ne divise pas $x$')
text(ax, 44, 6, r'aucun $g$ seul n’engendre $K$', 'limite', 'm')
save(fig, '59-033')
