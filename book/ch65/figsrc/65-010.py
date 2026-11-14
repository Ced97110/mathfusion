import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, r'$(r_1\ r_2\ r_3)$', 'sujet', 'xl')
xs = [16, 44, 72]
for k, x in enumerate(xs):
    box(ax, x - 8, 28, 16, 12, 'sujet', label=f'$r_{k + 1}$', size='m')
arrow(ax, (xs[0] + 8, 34), (xs[1] - 8, 34), 'varie')
arrow(ax, (xs[1] + 8, 34), (xs[2] - 8, 34), 'varie')
arrow(ax, (xs[2], 28), (xs[0], 28), 'varie', curve=-0.35)
brace(ax, 8, 80, 43.5, 'sujet', label='à lire dans l’ordre', down=False)
text(ax, 44, 8, 'retour sur $r_1$ : sous-entendu,\nnon écrit', 'varie', 's')
save(fig, '65-010')
