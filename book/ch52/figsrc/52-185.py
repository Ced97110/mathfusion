import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def row(y, vals, res, head, hrole, last):
    text(ax, 44, y + 17, head, hrole, 's')
    for i, (v, r) in enumerate(zip(vals, res)):
        role = last if i == 4 else 'fixe'
        box(ax, 6 + i * 16, y, 12, 11, role, label=f'{v}\n{r}', size='s')
        if i < 4: arrow(ax, (18.3 + i * 16, y + 5.5), (21.7 + i * 16, y + 5.5), 'varie')
row(40, [3, 7, 11, 15, 19], [3, 2, 1, 0, 4], 'reste voulu 4 par 5 : atteint', 'resultat', 'resultat')
row(10, [1, 5, 9, 13, 17], [1, 5, 3, 1, 5], 'reste voulu 0 par 6 : jamais', 'limite', 'limite')
text(ax, 44, 3, 'case : nombre, puis reste par n', 'fixe', 's')
save(fig, '52-185')
