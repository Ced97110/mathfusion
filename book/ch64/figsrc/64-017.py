import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 31, 66, r'$S_4$ : 24 permutations', 'fixe', 'm', weight='bold')
for r in range(4):
    for c in range(6):
        box(ax, 4 + 9 * c, 52 - 9 * r, 8, 8, 'sujet' if r < 2 else 'fixe', lw=0.7, r=0.6)
text(ax, 61, 47, r'$A_4$ : 12 paires', 'sujet', 's', ha='left', weight='bold')
text(ax, 61, 29, '12 impaires', 'fixe', 's', ha='left')
text(ax, 44, 12, '(12)(34) : 2 échanges = paire', 'varie', 's')
save(fig, '64-017')
