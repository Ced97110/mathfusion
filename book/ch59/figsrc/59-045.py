import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
box(ax, 3, 24, 12, 16, 'varie', label=r'$Q$', size='l')
arrow(ax, (16, 32), (25, 32), 'varie')
text(ax, 29, 36, r'$f_1$', 'varie', 'm'); text(ax, 29, 28, r'$f_2$', 'varie', 'm')
vals = [(4, 6), (6, 4)]
for i, row in enumerate(vals):
    for j, v in enumerate(row):
        box(ax, 33 + j * 10, 32 - i * 8 + 0, 10, 8, 'fixe', label=str(v))
text(ax, 38, 20, r'$e_1$', 'autre', 'm'); text(ax, 48, 20, r'$e_2$', 'autre', 'm')
box(ax, 72, 24, 12, 16, 'autre', label=r'$P$', size='l')
arrow(ax, (71, 32), (54, 32), 'autre')
text(ax, 22, 8, r'$QA$ : mélange les lignes', 'varie', 's')
text(ax, 66, 8, r'$AP$ : mélange les colonnes', 'autre', 's')
save(fig, '59-045')
