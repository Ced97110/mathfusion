import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
assert 0 * 1 % 2 == 0 and 2 * 1 % 2 == 0
# gauche : couples d'entiers, base, écriture unique
text(ax, 21, 66, 'couples d’entiers', 'sujet', 'm')
arrow(ax, (6, 36), (30, 36), 'sujet', lw=1.4)
arrow(ax, (6, 36), (6, 58), 'sujet', lw=1.4)
text(ax, 32, 36, '(1, 0)', 'sujet', 's', ha='left')
text(ax, 10, 58, '(0, 1)', 'sujet', 's', ha='left')
box(ax, 2, 10, 38, 14, 'resultat', label='(5, 4) : une seule\nécriture', size='s')
text(ax, 21, 4, 'libre', 'resultat', 'm', weight='bold')
# droite : l'horloge à deux heures
text(ax, 66, 66, 'horloge à 2 heures', 'autre', 'm')
disc(ax, 56, 44, 4.5, 'autre', label='0')
disc(ax, 78, 44, 4.5, 'autre', label='1')
arrow(ax, (73.5, 46.5), (60.5, 46.5), 'varie', lw=1.1, curve=0.5)
arrow(ax, (73.5, 41.5), (60.5, 41.5), 'varie', lw=1.1, curve=-0.5)
text(ax, 67, 56, r'$0\times 1$', 'varie', 's')
text(ax, 67, 31, r'$2\times 1$', 'varie', 's')
box(ax, 46, 10, 40, 14, 'limite', label='0 : deux écritures', size='s')
text(ax, 66, 4, 'pas libre', 'limite', 'm', weight='bold')
save(fig, '58-047')
