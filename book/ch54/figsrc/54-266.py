import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, 'Éléments non nuls de ℤ/8, produit', 'sujet', 's')
xs = [22 + i * 9.5 for i in range(7)]
for x, a in zip(xs, range(1, 8)):
    role = 'sujet' if a == 2 else 'autre' if a == 4 else 'fixe'
    disc(ax, x, 56, 4, role, label=str(a), size='s')
disc(ax, 8, 56, 4, 'fixe', fill=False, label='0', size='s')
box(ax, 20, 34, 48, 10, 'limite', label=r'$2\times4=8\equiv 0$', size='m')
arrow(ax, (xs[1], 51.6), (36, 44.6), 'sujet')
arrow(ax, (xs[3], 51.6), (52, 44.6), 'autre')
arrow(ax, (20, 39), (8, 51.5), 'limite', curve=-0.2)
text(ax, 44, 26, '0 n’est pas dans la liste', 'limite', 's')
text(ax, 44, 12, 'pas un groupe pour ×', 'limite', 'm', weight='bold')
brace(ax, xs[0] - 4, xs[-1] + 4, 49, 'fixe', label='non nuls', down=False) if False else None
save(fig, '54-266')
