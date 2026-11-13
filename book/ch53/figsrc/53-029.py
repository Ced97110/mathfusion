import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 2, 52, 24, 9, 'fixe', label='ALGEBRE')
box(ax, 2, 12, 24, 9, 'fixe', label='BONJOUR')
box(ax, 60, 30, 26, 11, 'varie', label='AAAAAAA')
arrow(ax, (26, 56.5), (60, 38.5), 'varie')
arrow(ax, (26, 16.5), (60, 32.5), 'varie')
text(ax, 36, 36, 'tout devient A', 'varie', 's')
# le retour : impossible, deux départs possibles
arrow(ax, (66, 29), (26, 14), 'limite', curve=-0.25)
arrow(ax, (68, 42), (26, 60), 'limite', curve=0.25)
text(ax, 73, 22, 'retour :', 'limite', 's')
text(ax, 73, 18, 'lequel ?', 'limite', 's', weight='bold')
save(fig, '53-029')
