import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
y = 28
disc(ax, 8, y, 1.6); disc(ax, 80, y, 1.6)
line(ax, [(8, y), (34, y)]); line(ax, [(54, y), (80, y)])
line(ax, [(34, y), (39, y + 6)], 'limite', lw=1.2)
line(ax, [(54, y), (49, y - 4)], 'limite', lw=1.2) if False else None
text(ax, 44, y + 11, r'$O$', 'limite', 'xl', weight='bold')
text(ax, 44, y - 8, 'fil coupé : jamais de courant', 'limite', 's')
text(ax, 44, 6, 'partie vide : aucune branche', 'sujet', 's')
text(ax, 44, y + 4, '', 'fixe', 's') if False else None
save(fig, '80-197')
