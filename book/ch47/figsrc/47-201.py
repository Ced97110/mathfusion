import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cols = [(15, 'Horloge 5', 'resultat', '5 él.', None),
        (44, 'Horloge 12', 'limite', '12 él.', '4 él.'),
        (73, 'Carré', 'limite', '8 él.', '4 rotations')]
for x, t, r, top, mid in cols:
    text(ax, x, 65, t, 'encre', 's', weight='bold')
    box(ax, x - 11, 50, 22, 7, r, label=top, size='s')
    box(ax, x - 11, 6, 22, 7, 'fixe', label=r'$\{1\}$', size='s')
    if mid:
        box(ax, x - 11, 28, 22, 7, 'sujet', label=mid, size='s')
        line(ax, [(x, 35), (x, 50)], 'fixe'); line(ax, [(x, 13), (x, 28)], 'fixe')
    else:
        line(ax, [(x, 13), (x, 50)], 'fixe')
text(ax, 15, 35, 'rien entre', 'resultat', 's'); text(ax, 15, 29.5, 'les deux', 'resultat', 's')
text(ax, 44, 21, 'normal au milieu', 'limite', 's'); text(ax, 73, 21, 'normal au milieu', 'limite', 's')
save(fig, '47-201')
