import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 2, 33, 'cahiers', 'sujet', 's', ha='left'); text(ax, 2, 9, 'euros', 'resultat', 's', ha='left')
xs = [22, 36, 50, 64]
for x, a, b in zip(xs, [0, 1, 2, 10], [1, 3, 5, 21]):
    box(ax, x - 6, 28, 12, 10, 'sujet', label=str(a), size='l')
    box(ax, x - 6, 4, 12, 10, 'resultat', label=str(b), size='l')
    arrow(ax, (x, 28), (x, 15), 'varie')
box(ax, 72, 28, 12, 10, 'fixe', dash=True, label='…', size='l'); box(ax, 72, 4, 12, 10, 'fixe', dash=True, label='…', size='l')
arrow(ax, (66, 44), (84, 44), 'varie'); text(ax, 75, 47, 'sans fin', 'varie', 's')
save(fig, '19-006')
