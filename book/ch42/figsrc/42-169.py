import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'$S=\{x,\ y\}$ en première place', 'sujet', 'm', weight='bold')
text(ax, 4, 52, r'$T=\{1\}$', 'autre', 'm', ha='left')
text(ax, 4, 22, r'$T=\emptyset$', 'limite', 'm', ha='left')
for x, n in zip((38, 54), ('x', 'y')):
    disc(ax, x, 52, 2.6, 'autre')
    text(ax, x, 45, rf'$({n},1)$', 'autre', 's')
box(ax, 28, 16, 36, 12, 'fixe', fill=False, dash=True, label='aucun couple', size='s')
text(ax, 46, 9, 'aucun second terme possible', 'limite', 's')
line(ax, [(2, 40), (86, 40)], 'fixe', lw=0.5, dash=True)
text(ax, 76, 52, r'$2\times1=2$', 'autre', 'm'); text(ax, 76, 22, r'$2\times0=0$', 'resultat', 'm', weight='bold')
save(fig, '42-169')
