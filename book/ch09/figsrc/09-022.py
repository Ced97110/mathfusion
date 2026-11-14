import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
vals = ['8', '254', r'$2/5$', '0,07']
text(ax, 44, 46, 'aucune unité derrière', 'sujet', 'm', weight='bold')
text(ax, 11, 32, 'nombre', 'sujet', 's'); text(ax, 11, 14, 'unité', 'fixe', 's')
for i, v in enumerate(vals):
    x = 24 + i * 16
    box(ax, x, 27, 14, 10, 'sujet', label=v)
    box(ax, x, 9, 14, 10, 'fixe', fill=False, dash=True, label='rien', size='s')
save(fig, '09-022')
