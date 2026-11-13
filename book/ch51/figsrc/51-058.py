import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, 'dans les entiers', 'fixe', 'm')
for k, v in enumerate(range(-3, 4)):
    x = 5 + k * 11.5
    unit = v in (-1, 1)
    box(ax, x, 22, 10, 11, 'sujet' if unit else 'fixe', label=str(v).replace('-', '−'), size='l')
    if unit: text(ax, x + 5, 17, 'unité', 'sujet', 's')
text(ax, 44, 6, 'unité = élément qui a un inverse', 'sujet', 'm')
save(fig, '51-058')
