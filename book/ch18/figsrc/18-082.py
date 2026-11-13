import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 8, 60, 'avant', 'fixe', 's', ha='left'); text(ax, 8, 28, 'après', 'fixe', 's', ha='left')
xs = [30, 52, 74]
for x, a, b, s in zip(xs, ['18', '56', '6'], ['9', '28', '3'], ['$x^2$', '$x$', '']):
    box(ax, x - 8, 48, 16, 9, 'sujet', label=a)
    arrow(ax, (x, 48), (x, 41), 'varie')
    text(ax, x + 2, 44.5, r'$\div2$', 'varie', 's', ha='left')
    box(ax, x - 8, 30, 16, 9, 'resultat', label=b)
box(ax, 4, 6, 14, 9, 'varie', label='2')
text(ax, 22, 10.5, 'retiré devant : les nombres rétrécissent', 'varie', 's', ha='left')
save(fig, '18-082')
