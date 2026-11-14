import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def grid(x, y, k, c, role):
    poly(ax, [(x, y), (x + k * c, y), (x + k * c, y + k * c), (x, y + k * c)], role)
    for i in range(1, k):
        line(ax, [(x + i * c, y), (x + i * c, y + k * c)], role, lw=0.6)
        line(ax, [(x, y + i * c), (x + k * c, y + i * c)], role, lw=0.6)
text(ax, 44, 54, r'lignes = colonnes = $m+n$', 'sujet', 'm', weight='bold')
grid(4, 24, 2, 8, 'fixe')
text(ax, 12, 17, '$2\\times2$\ndeux droites', 'fixe', 's')
grid(28, 24, 3, 8, 'fixe')
text(ax, 40, 17, '$3\\times3$\n$m+n=3$', 'fixe', 's')
grid(60, 24, 4, 6, 'sujet')
text(ax, 72, 17, r'$m+n$ colonnes', 'sujet', 's')
text(ax, 56, 36, r'$m+n$ lignes', 'sujet', 's', rot=90)
save(fig, '70-037')
