import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 3, 67, 'diviseurs de 12', 'fixe', 's', ha='left')
xs = [2 + 14.6 * i for i in range(6)]
for x, n in zip(xs, ['1', '2', '3', '4', '6', '12']):
    box(ax, x, 52, 11, 8, 'sujet' if n in ('4', '12') else 'fixe', label=n, size='s')
brace(ax, xs[3] + 5.5, xs[5] + 5.5, 51, 'resultat', label='entre 4 et 12 : aucun')
text(ax, 3, 42, 'dans les diviseurs de 60', 'fixe', 's', ha='left')
for c, n in [(14, '4'), (44, '12'), (74, '60')]: box(ax, c - 7, 14, 14, 8, 'sujet', label=n, size='s')
arrow(ax, (22, 18), (36, 18), 'resultat'); text(ax, 29, 8, '12 recouvre 4', 'resultat', 's')
arrow(ax, (52, 18), (66, 18), 'fixe')
arrow(ax, (14, 23), (74, 23), 'limite', curve=-0.3); text(ax, 44, 34, '60 ne recouvre pas 4', 'limite', 's')
save(fig, '79-032')
