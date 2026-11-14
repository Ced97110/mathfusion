import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
xs = [5, 24, 43, 62]
for i, x in enumerate(xs): box(ax, x, 62, 17, 10, 'fixe' if i < 2 else 'varie', label=str(i + 1), size='l')
brace(ax, 5, 40, 72, 'fixe', label=r'$T$ : fixés', down=False)
brace(ax, 43, 79, 72, 'varie', label='libres', down=False)
arrow(ax, (58, 60), (38, 47), 'varie'); arrow(ax, (64, 60), (66, 47), 'varie')
box(ax, 29, 36, 18, 10, 'varie', label='3 4', size='m'); box(ax, 57, 36, 18, 10, 'varie', label='4 3', size='m')
text(ax, 52, 26, r'$2!=2$ façons', 'resultat', 'm')
text(ax, 44, 10, r'$T$ vide : $4!=24$ façons', 'fixe', 's')
save(fig, '80-374')
