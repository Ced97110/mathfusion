import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
X = [16, 44, 72]
for x, s, r in zip(X, ['4,37', '3,22', '7,59'], ['sujet', 'sujet', 'resultat']):
    text(ax, x, 72, s, r, 'xl', weight='bold')
text(ax, 30, 72, '+', 'encre', 'xl'); text(ax, 58, 72, '=', 'encre', 'xl')
for x, s, r in zip(X, [r'$\frac{437}{100}$', r'$\frac{322}{100}$', r'$\frac{759}{100}$'], ['sujet', 'sujet', 'resultat']):
    box(ax, x - 11, 36, 22, 16, r, label=s, size='l')
text(ax, 30, 44, '+', 'encre', 'xl'); text(ax, 58, 44, '=', 'encre', 'xl')
arrow(ax, (16, 66), (16, 53), 'varie'); arrow(ax, (44, 66), (44, 53), 'varie')
text(ax, 19, 60, 'en centièmes', 'varie', 's', ha='left')
arrow(ax, (72, 53), (72, 66), 'resultat')
box(ax, 4, 8, 38, 14, 'varie', label='hauts : 437 + 322 = 759', size='s')
box(ax, 46, 8, 38, 14, 'fixe', label='bas : 100, inchangé', size='s')
arrow(ax, (16, 35), (20, 23), 'varie'); arrow(ax, (72, 35), (66, 23), 'fixe')
save(fig, '08-049')
