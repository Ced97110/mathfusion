import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 2, 84, 60, 'sujet', lw=1.1)
text(ax, 44, 55, r'$E(2)$ : tous les déplacements', 'sujet', 'l')
names = ['glissements', 'rotations', 'réflexions', 'symétries glissées']
for i, n in enumerate(names):
    x = 6 + (i % 2) * 40; y = 32 - (i // 2) * 14
    box(ax, x, y, 36, 10, 'autre' if i % 2 else 'varie', label=n, size='s')
box(ax, 14, 6, 60, 10, 'resultat', label=r'chacun s’écrit $Ax+b$', size='m')
save(fig, '74-097')
