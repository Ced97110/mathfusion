import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
labs = [r'$a_{1}$', r'$a_{2}$', r'$a_{3}$', r'$\cdots$', r'$a_{n}$']
bw, g = 12, 3; x0 = (88 - (5 * bw + 4 * g)) / 2
for k, s in enumerate(labs):
    box(ax, x0 + k * (bw + g), 28, bw, 11, 'fixe' if k == 3 else 'sujet', label=s, size='l')
xr = x0 + 4 * (bw + g)
brace(ax, x0, xr + bw, 26, 'sujet', label=r'$n$ éléments', down=True)
text(ax, 6, 59, 'Liste numérotée', 'sujet', 'm', weight='bold', ha='left')
arrow(ax, (xr + bw / 2 + 1, 51.5), (xr + bw / 2 + 1, 40.5), 'varie')
text(ax, 85, 53.5, 'numéro = place', 'varie', 's', ha='right')
arrow(ax, (x0 + 3 * (bw + g) + bw / 2, 44.5), (x0 + 3 * (bw + g) + bw / 2, 40.5), 'fixe')
text(ax, x0 + 3 * (bw + g) + bw / 2 + 2, 46, 'le reste', 'fixe', 's', ha='right')
text(ax, 44, 7, r'cent éléments : $n = 100$', 'encre', 's')
save(fig, '45-102')
