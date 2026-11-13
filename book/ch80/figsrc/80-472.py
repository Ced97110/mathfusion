import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
box(ax, 4, 14, 36, 36, 'fixe', r=2.0)
line(ax, [(8, 18), (36, 46)], 'sujet', lw=1.8); line(ax, [(8, 40), (36, 24)], 'autre', lw=1.8)
disc(ax, 22, 32, 1.8, 'varie')
text(ax, 22, 54, 'deux droites du plan', 'encre', 's')
text(ax, 37, 19, r'droite', 'sujet', 's', ha='right'); text(ax, 9, 45, r'droite', 'autre', 's', ha='left')
text(ax, 31, 33, 'origine', 'varie', 's')
items = [(50, 'fixe', 'somme : 2'), (50, 'varie', 'commun : 0'), (50, 'sujet', 'droite : 1'), (50, 'autre', 'droite : 1')]
box(ax, 46, 44, 38, 8, 'fixe', label='somme : 2'); box(ax, 46, 32, 38, 8, 'varie', label='commun : 0')
text(ax, 65, 27.5, r'$2+0=1+1$', 'encre', 'm')
box(ax, 46, 14, 38, 8, 'sujet', label='droite : 1'); box(ax, 46, 3, 38, 8, 'autre', label='droite : 1')
text(ax, 65, 24.5, '= 1 + 1', 'encre', 's') if False else None
save(fig, '80-472')
