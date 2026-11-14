import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$(\mathbb{N},\,\times,\,1)$', 'sujet', 'xl')
box(ax, 4, 40, 38, 11, 'resultat', label=r'$1\times 5=5$', size='m')
text(ax, 23, 36, '1 est neutre', 'resultat', 's')
box(ax, 46, 40, 38, 11, 'limite', label=r'$2\times ?=1$', size='m')
text(ax, 65, 36, 'aucun entier ne convient', 'limite', 's')
f = numberline(ax, 10, 66, 16, 0, 4, arrow_right=True)
for v in range(5): disc(ax, f(v), 16, 1.1, 'sujet')
disc(ax, f(0.5), 16, 1.1, 'limite', fill=False)
text(ax, f(0.5), 24, '½', 'limite', 'm'); arrow(ax, (f(0.5), 22), (f(0.5), 18), 'limite')
text(ax, f(2.6), 24, 'pas dans ℕ', 'limite', 's') if False else None
text(ax, f(3), 24, '½ n’est pas dans ℕ', 'limite', 's', ha='center')
save(fig, '44-070')
