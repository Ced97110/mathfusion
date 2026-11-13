import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'un 5-cycle : $(1\ 3\ 5\ 2\ 4)$', 'sujet', 'm')
xs = [10 + i * 14 for i in range(5)]; seq = ['1', '3', '5', '2', '4']
for i, (x, s) in enumerate(zip(xs, seq)):
    box(ax, x - 5, 34, 10, 9, 'fixe' if i == 0 else 'sujet', label=s, size='l', weight='bold')
text(ax, xs[0], 46.5, 'en tête', 'fixe', 's')
for c, x in zip([4, 3, 2, 1], xs[1:]):
    arrow(ax, (x, 33.2), (x, 25.8), 'varie')
    text(ax, x, 22.5, str(c), 'varie', 'l', weight='bold')
text(ax, 62, 15.5, 'choix pour chaque place', 'varie', 's')
box(ax, 16, 3, 56, 8, 'resultat', label=r'$4 \times 3 \times 2 \times 1 = 24$', size='m', weight='bold')
save(fig, '50-149')
