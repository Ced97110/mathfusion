import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
Z = r'$\mathbb{Z}$'
box(ax, 6, 84, 76, 10, 'fixe', label=r'$12^7$ applications à essayer ?', size='m')
text(ax, 44, 78, 'trop long : on trie par le noyau', 'limite', 's')
box(ax, 6, 58, 76, 10, 'varie', label=r'noyaux : $\{0\}$ ou $\mathbb{Z}/7\mathbb{Z}$', size='m')
box(ax, 6, 36, 76, 10, 'sujet', label=r'quotients : 7 ou 1 éléments', size='m')
box(ax, 6, 8, 36, 12, 'limite', label=r'7 éléments : écarté', size='s')
box(ax, 46, 8, 36, 12, 'resultat', label=r'1 élément : gardé', size='s')
arrow(ax, (44, 74), (44, 68.5), 'fixe'); arrow(ax, (44, 58), (44, 46.5), 'varie')
text(ax, 62, 52.5, 'lister les noyaux', 'varie', 's', ha='left') if False else None
text(ax, 62, 51.5, 'image = quotient', 'varie', 's', ha='left')
arrow(ax, (30, 36), (24, 20.5), 'fixe'); arrow(ax, (58, 36), (64, 20.5), 'fixe')
text(ax, 44, 28, r'dans $\mathbb{Z}/12\mathbb{Z}$ ?', 'encre', 's')
save(fig, '48-164')
