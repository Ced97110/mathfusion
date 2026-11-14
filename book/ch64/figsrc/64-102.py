import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
RO = {2: 'sujet', 3: 'varie', 5: 'resultat'}
for y, cap, fs in ((50, 'suite 1', [3, 5, 2, 2]), (34, 'suite 2', [2, 2, 5, 3])):
    text(ax, 3, y, cap, 'encre', 's', ha='left')
    for k, f in enumerate(fs):
        disc(ax, 30 + k * 14, y, 4.5, RO[f], label=str(f), size='l')
    line(ax, [(34.5 + 3 * 14, y), (82, y), (82, 14)], 'fixe', lw=0.9)
box(ax, 14, 8, 60, 12, 'resultat', label=r'$2\times2\times3\times5=60$', size='m')
arrow(ax, (82, 14), (74.5, 14), 'fixe')
save(fig, '64-102')
