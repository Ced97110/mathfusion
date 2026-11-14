import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
disc(ax, 26, 56, 8, 'fixe', label='0', size='l'); disc(ax, 62, 56, 8, 'sujet', label='1', size='l')
arrow(ax, (35, 56), (53, 56), 'varie', both=True)
text(ax, 26, 44, 'ouvert', 'fixe', 'm'); text(ax, 62, 44, 'fermé', 'sujet', 'm')
for x, h, s in ((2, 'ou', r'$1 \vee 1 = 1$'), (32, 'et', r'$1 \times 1 = 1$'), (62, 'non', r'non $1 = 0$')):
    text(ax, x + 12, 32, h, 'varie', 'm'); box(ax, x, 14, 24, 12, 'resultat', label=s, size='s')
text(ax, 44, 6, 'trois opérations, deux valeurs', 'encre', 's')
save(fig, '80-329')
