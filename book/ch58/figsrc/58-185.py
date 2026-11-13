import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# polynômes de départ 1, x, x^2, ... : n + 1 briques
def brick(x, y, lab):
    box(ax, x, y, 14, 10, 'sujet', label=lab, size='m', r=0.6)
w = 16.5
# degré au plus 2 : le polynôme 3 + 4x + 5x^2
text(ax, 44, 79, r'degré au plus 2 : $3 + 4x + 5x^2$', 'encre', 's')
for i, lab in enumerate(['1', r'$x$', r'$x^2$']):
    brick(10 + i * w, 56, lab)
    box(ax, 10 + i * w + 2, 44, 10, 8, 'varie', label=str([3, 4, 5][i]), size='m', r=0.5)
    line(ax, [(17 + i * w, 52), (17 + i * w, 56)], 'varie', lw=0.8)
brace(ax, 10, 10 + 2 * w + 14, 42, 'resultat', label='3 briques', down=True)
text(ax, 76, 56 + 5, 'dim = 3', 'resultat', 's', weight='bold')
# degré au plus 3
text(ax, 44, 26, 'degré au plus 3', 'encre', 's')
for i, lab in enumerate(['1', r'$x$', r'$x^2$', r'$x^3$']):
    brick(10 + i * 16.8, 11, lab)
brace(ax, 10, 10 + 3 * 16.8 + 14, 9, 'resultat', label=r'4 briques = $n + 1$', down=True)
save(fig, '58-185')
