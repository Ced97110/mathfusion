import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# gauche : un corps qui en contient un autre
box(ax, 3, 14, 36, 36, 'sujet')
text(ax, 21, 44, r'$\mathbb{Q}(\sqrt{2})$', 'sujet', 'm', weight='bold')
box(ax, 9, 19, 24, 16, 'fixe', label=r'$\mathbb{Q}$', size='l')
text(ax, 21, 8, 'contient les fractions', 'fixe', 's')
# droite : un nombre a + b√2 a deux coordonnées
text(ax, 64, 56, r'$a + b\sqrt{2}$', 'sujet', 'l', weight='bold')
box(ax, 47, 28, 14, 14, 'fixe', label=r'$a$', size='l')
box(ax, 65, 28, 14, 14, 'varie', label=r'$b$', size='l')
text(ax, 54, 46, r'$\times\,1$', 'fixe', 's')
text(ax, 72, 46, r'$\times\,\sqrt{2}$', 'varie', 's')
brace(ax, 47, 79, 25, 'resultat', label='2 cases', down=True)
text(ax, 63, 8, r'dimension $2$ sur $\mathbb{Q}$', 'resultat', 'm', weight='bold')
save(fig, '58-336')
