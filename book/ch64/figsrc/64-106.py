import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 8, 70, r'$G$ : $8=2^3$ éléments', 'sujet', 'm', ha='left')
for k in range(8):
    box(ax, 8 + k * 9, 52, 8, 9, 'varie' if k < 2 else 'sujet')
brace(ax, 8, 25, 52, 'varie', label='$C$ non trivial : 2 éléments', size='s')
arrow(ax, (44, 46), (44, 38), 'fixe')
text(ax, 47, 42, r'ôter $C$', 'fixe', 's', ha='left')
text(ax, 8, 36.5, r'$G/C$ : $4=2^2$', 'sujet', 'm', ha='left')
for k in range(4):
    box(ax, 8 + k * 18, 20, 17, 9, 'sujet')
box(ax, 8, 2, 71, 9, 'fixe', dash=True, label='on recommence avec $G/C$ jusqu\'à 1', size='s')
arrow(ax, (44, 19), (44, 12), 'fixe')
save(fig, '64-106')
