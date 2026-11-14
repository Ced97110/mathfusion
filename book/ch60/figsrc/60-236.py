import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
xs = [3, 31, 59]
cols = [(r'$2^2$', [('2', '4'), ('1 + 1', '2 et 2')]),
        (r'$3^3$', [('3', '27'), ('2 + 1', '9 et 3'), ('1 + 1 + 1', '3, 3 et 3')]),
        (r'$5^1$', [('1', '5')])]
for x, (h, items) in zip(xs, cols):
    text(ax, x + 13, 92, h, 'sujet', 'l', weight='bold')
    for k, (p, o) in enumerate(items):
        box(ax, x, 68 - 17 * k, 26, 15, 'sujet', label=p + '\n' + o)
text(ax, 44, 24, 'dessous : ordre des morceaux', 'fixe', 's')
text(ax, 44, 12, r'$2\times3\times1=6$ groupes', 'resultat', 'l', weight='bold')
save(fig, '60-236')
