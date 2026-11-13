import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 22, 92, '3,2', 'sujet', 'xl', weight='bold'); text(ax, 44, 92, r'$\times$', 'encre', 'xl'); text(ax, 66, 92, '1,46', 'sujet', 'xl', weight='bold')
text(ax, 22, 82, '1 décimale', 'sujet', 's'); text(ax, 66, 82, '2 décimales', 'sujet', 's')
box(ax, 14, 58, 60, 12, 'varie', label=r'$32\times146=4\,672$', size='l')
text(ax, 80, 64, 'sans virgule', 'varie', 's', ha='right') if False else None
arrow(ax, (44, 88), (44, 71), 'varie')
box(ax, 14, 36, 60, 10, 'fixe', label='1 + 2 = 3 décimales', size='m')
arrow(ax, (44, 57), (44, 47), 'fixe')
cx = [24, 38, 48, 58]; xs = [22, 36, 46, 56]
for x, d in zip([22, 38, 48, 58], '4672'):
    box(ax, x - 4.5, 10, 9, 11, 'resultat', label=d, size='l')
text(ax, 30, 15.5, ',', 'resultat', 'xl', weight='bold')
brace(ax, 33.5, 62.5, 8, 'varie', label='3 chiffres après la virgule')
arrow(ax, (44, 35), (44, 22.5), 'varie')
save(fig, '08-050')
