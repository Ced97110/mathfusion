import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
eq = [r'$3x-3+4x^2=4x^2+x+5$', r'$3x-3=x+5$', r'$2x-3=5$', r'$2x=8$', r'$x=4$']
act = [r'retirer $4x^2$', r'retirer $x$', r'ajouter 3', r'diviser par 2']
ys = [66 - 15 * i for i in range(5)]
for i, (s, y) in enumerate(zip(eq, ys)):
    box(ax, 4, y - 4, 46, 9, 'resultat' if i == 4 else ('sujet' if i == 0 else 'fixe'), label=s, size='s')
    if i < 4:
        arrow(ax, (27, y - 5), (27, ys[i + 1] + 5.5), 'varie')
        text(ax, 68, y - 10, act[i], 'varie', 's')
save(fig, '21-123')
