import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# un inconnu -> message signé « Bob » -> Alice
box(ax, 2, 28, 22, 12, 'fixe', label='Un inconnu')
box(ax, 30, 26, 28, 16, 'varie', label='Message\nsigné « Bob »')
box(ax, 64, 28, 22, 12, 'sujet', label='Alice')
arrow(ax, (24.5, 34), (29.5, 34), 'fixe')
arrow(ax, (58.5, 34), (63.5, 34), 'fixe')
text(ax, 75, 22, 'clé d’Alice :', 'sujet', 's')
text(ax, 75, 18.5, 'publique', 'sujet', 's')
# Bob possible, mais rien ne le prouve
box(ax, 30, 4, 28, 10, 'autre', label='Bob ?', dash=True)
arrow(ax, (44, 14.5), (44, 25.5), 'autre')
text(ax, 44, 51, 'Qui a vraiment écrit ?', 'varie', 'm', weight='bold')
text(ax, 13, 22, 'peut être', 'fixe', 's')
text(ax, 13, 18.5, 'n’importe qui', 'fixe', 's')
save(fig, '53-144')
