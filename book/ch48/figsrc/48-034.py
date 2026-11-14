import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = [14 + i * 20 for i in range(4)]
for x, n, r in zip(xs, ['0', '1', '2', '3'], ['0°', '90°', '180°', '270°']):
    disc(ax, x, 54, 5, 'sujet', label=n, size='m')
    disc(ax, x, 12, 5, 'autre', label=r, size='s')
    arrow(ax, (x, 48.5), (x, 17.5), 'varie', lw=1.1, both=True)
text(ax, 44, 33, r'$\cong$', 'resultat', 'xl')
text(ax, 4, 63, r'$G$ : positions', 'sujet', 's', ha='left')
text(ax, 4, 3, r"$G'$ : rotations du carré", 'autre', 's', ha='left')
save(fig, '48-034')
