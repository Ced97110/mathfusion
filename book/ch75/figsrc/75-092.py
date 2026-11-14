import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'6 éléments : permutations de 3 objets', 'encre', 'm')
box(ax, 8, 33, 72, 20, 'sujet', fill=False, dash=True)
for i in range(3): disc(ax, 22 + i * 22, 43, 4, 'sujet')
text(ax, 44, 57, '', 'sujet', 's')
text(ax, 44, 28.5, 'commutateurs : neutre + 2 rotations', 'sujet', 's')
for i in range(3): disc(ax, 22 + i * 22, 14, 4, 'limite')
text(ax, 44, 5, '3 échanges : jamais obtenus', 'limite', 's')
arrow(ax, (44, 25), (44, 21), 'limite', lw=0.8) if False else None
save(fig, '75-092')
