import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 3, 64, 24, 10, 'sujet', label='13 × 17')
arrow(ax, (28, 69), (40, 69), 'varie', lw=1.3)
text(ax, 34, 77, 'un calcul', 'varie', 's')
box(ax, 41, 64, 24, 10, 'resultat', label='221')
box(ax, 3, 40, 24, 10, 'resultat', label='221')
text(ax, 58, 45, "dans l'autre sens", 'encre', 'm')
arrow(ax, (15, 39), (15, 31), 'varie', lw=1.3)
vals = ['2', '3', '5', '7', '11', '13']
for k, v in enumerate(vals):
    box(ax, 5 + k * 13.4, 12, 11, 10, 'resultat' if v == '13' else 'fixe', label=v)
brace(ax, 5, 83, 25, 'fixe', label='6 essais', down=False)
save(fig, '53-009')
