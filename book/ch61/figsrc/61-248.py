import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 20, 46, 48, 11, 'sujet', label='critère de Galois')
box(ax, 3, 8, 38, 24, 'resultat'); box(ax, 47, 8, 38, 24, 'limite')
text(ax, 22, 26, 'degré 2', 'resultat', 'm'); text(ax, 22, 18, 'résoluble', 'resultat', 's'); text(ax, 22, 12.5, 'par radicaux', 'resultat', 's')
text(ax, 66, 26, 'degré 5 général', 'limite', 'm'); text(ax, 66, 18, 'non résoluble', 'limite', 's'); text(ax, 66, 12.5, 'par radicaux', 'limite', 's')
arrow(ax, (36, 46), (22, 32.8), 'varie'); arrow(ax, (52, 46), (66, 32.8), 'varie')
text(ax, 44, 38, 'dit quand', 'varie', 's')
save(fig, '61-248')
