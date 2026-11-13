import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [4 + i * 9 for i in range(9)]
for i, x in enumerate(xs):
    box(ax, x, 46, 8, 9, 'sujet' if i % 4 == 0 else 'fixe', label=str(i), size='s')
text(ax, 44, 62, 'nombres de quarts de tour', 'fixe', 's')
disc(ax, 44, 20, 6, 'resultat', label='0')
for i in (0, 4, 8): arrow(ax, (xs[i] + 4, 45), (44 + (xs[i] - 40) * 0.12, 26.5), 'varie')
text(ax, 44, 8, 'neutre de G′ : position 0', 'resultat', 's')
text(ax, 70, 30, r'$\ker f$ : cases bleues', 'sujet', 's')
save(fig, '48-029')
