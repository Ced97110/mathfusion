import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 2, 84, 60, role='sujet', label=None)
text(ax, 44, 56.5, 'Jacobson : séparable ET normale', 'sujet', 'm', weight='bold')
box(ax, 8, 6, 72, 40, role='autre', label=None)
text(ax, 44, 41, 'Judson : F fini ou de car. 0', 'autre', 'm', weight='bold')
box(ax, 14, 22, 60, 11, role='resultat', label='✓ séparable : automatique')
box(ax, 14, 9, 60, 11, role='varie', label='normale : à vérifier')
save(fig, '63-132')
