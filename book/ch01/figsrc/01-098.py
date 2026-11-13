import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
line(ax, [(31, 52), (43, 46), (31, 40)], 'sujet', lw=2.2)
text(ax, 37, 58, 'plus grand que', 'sujet', 's')
line(ax, [(31, 36), (43, 36)], 'autre', lw=2.2)
text(ax, 37, 31.5, 'ou égal à', 'autre', 's')
text(ax, 20, 46, 'témoin', 'encre', 'l'); text(ax, 50, 46, '5', 'encre', 'l')
text(ax, 6, 26.5, 'valeurs du témoin', 'fixe', 's', ha='left')
box(ax, 6, 14, 30, 8, 'fixe', fill=False, label='0 à 4', size='m')
box(ax, 38, 14, 8, 8, 'autre', label='5', size='m')
for i, d in enumerate('6789'):
    box(ax, 46 + 8 * i, 14, 8, 8, 'sujet', label=d, size='m')
brace(ax, 38, 78, 12, 'resultat', label='5 ou plus : on ajoute 1', down=True, size='s')
save(fig, '01-098')
