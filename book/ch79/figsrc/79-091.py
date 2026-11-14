import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# groupe : une opération ; anneau : deux opérations
box(ax, 2, 40, 28, 26, 'fixe', fill=False)
text(ax, 16, 60, 'groupe', 'fixe', 'm', weight='bold'); disc(ax, 16, 48, 4, 'fixe', label='+', size='l')
box(ax, 2, 6, 28, 30, 'fixe', fill=False)
text(ax, 16, 30, 'anneau', 'fixe', 'm', weight='bold')
disc(ax, 10, 17, 4, 'fixe', label='+', size='l'); disc(ax, 22, 17, 4, 'fixe', label=r'$\times$', size='l')
# treillis : deux opérations et quatre lois, aucun ordre
box(ax, 36, 6, 50, 60, 'sujet', fill=False, lw=1.2)
text(ax, 61, 60, 'treillis', 'sujet', 'l', weight='bold')
disc(ax, 51, 49, 4, 'sujet', label=r'$\vee$', size='l'); disc(ax, 71, 49, 4, 'sujet', label=r'$\wedge$', size='l')
for i, t in enumerate(['L1 : commutativité', 'L2 : associativité', 'L3 : idempotence', 'L4 : absorption']):
    text(ax, 40, 38 - i * 6.2, t, 'sujet', 's', ha='left')
text(ax, 61, 9.5, 'aucun ordre au départ', 'encre', 's', weight='bold')
save(fig, '79-091')
