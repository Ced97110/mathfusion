import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 44, 91, 'dimension 4 : deux paires', 'encre', 's')
def row(y, a, b):
    box(ax, 4, y, 38, 12, *a); box(ax, 46, y, 38, 12, *b)
row(72, ('sujet', True, 'paire 1'), ('fixe', True, 'reste : dimension 2'))
arrow(ax, (23, 71), (23, 59.5), 'varie'); text(ax, 60, 65.5, r'$(u,v)\to(u^\prime,v^\prime)$', 'varie', 's')
row(46, ('resultat', True, 'paire 1 réglée'), ('sujet', True, 'paire 2'))
arrow(ax, (65, 45), (65, 33.5), 'varie'); text(ax, 30, 39.5, 'même étape, plus petit', 'varie', 's')
row(20, ('resultat', True, 'paire 1 réglée'), ('resultat', True, 'paire 2 réglée'))
text(ax, 44, 10, '2 tours pour 4 dimensions', 'resultat', 's')
save(fig, '75-080')
