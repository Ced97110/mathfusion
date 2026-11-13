import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
bw, gap, y = 18, 3.5, 50
xs = [2.75 + i * (bw + gap) for i in range(4)]
labs = ['division\navec reste', 'Bézout', 'lemme\nd’Euclide', 'factorisation\nunique']
for i, (x, t) in enumerate(zip(xs, labs)):
    box(ax, x, y, bw, 12, 'resultat' if i == 3 else 'sujet', label=t, size='s')
    if i < 3: arrow(ax, (x + bw + 0.3, y + 6), (x + bw + gap - 0.3, y + 6), 'varie')
brace(ax, xs[0], xs[3] + bw, y + 13, 'sujet', 'la même chaîne dans chacun', down=False)
# les deux cas
box(ax, 2, 6, 84, 28, 'resultat', fill=False, dash=True)
text(ax, 44, 30, 'anneaux euclidiens', 'resultat', 's', weight='bold')
box(ax, 6, 9, 46, 16, 'fixe')
text(ax, 11, 21, 'entiers', 'encre', 's', ha='left')
text(ax, 11, 13.5, '12 =', 'encre', 's', ha='left')
for k, t in enumerate(['2', '2', '3']):
    disc(ax, 26 + k * 8.5, 13.5, 3, 'sujet', label=t, size='s')
box(ax, 56, 9, 26, 16, 'fixe', label='polynômes', size='s')
arrow(ax, (xs[0] + bw / 2, 34.6), (xs[0] + bw / 2, y - 0.3), 'varie')
save(fig, '05-180')
