import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'Cinq bits : 11011', 'sujet', 'm')
for i, b in enumerate('11011'):
    box(ax, 4 + i * 16, 44, 14, 12, 'sujet', label=b, size='l')
text(ax, 11, 38, '1 : 16 utilisé', 'sujet', 's', ha='left')
text(ax, 44, 28, 'valeurs possibles', 'encre', 's')
box(ax, 2, 8, 26, 14, 'autre', label='lettre : 26', size='s')
box(ax, 31, 8, 27, 14, 'autre', label='chiffre : 10', size='s')
box(ax, 61, 8, 25, 14, 'sujet', label='bit : 2', size='s')
save(fig, '53-115')
