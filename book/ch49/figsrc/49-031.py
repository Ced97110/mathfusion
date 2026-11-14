import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 28, 56, r'$FM^{(r)}$', 'sujet', 'xl', weight='bold')
text(ax, 62, 56, '', 'encre', 's')
brace(ax, 18, 33, 52, 'sujet', label='tous les mots', depth=1.4)
text(ax, 62, 56, r'$r$ : nombre de lettres', 'varie', 's')
for y, n in ((26, 2), (8, 5)):
    for i in range(n): disc(ax, 8 + i * 7, y + 4, 2.4, 'fixe')
    text(ax, 8 + (n - 1) * 3.5, y - 3, f'{n} lettres', 'fixe', 's')
    arrow(ax, (46, y + 4), (54, y + 4), 'varie')
    text(ax, 70, y + 4, rf'$FM^{{({n})}}$', 'sujet', 'l')
save(fig, '49-031')
