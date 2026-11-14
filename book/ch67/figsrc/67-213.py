import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 4, 48, 50, 18, 'varie', fill=False, dash=True)
text(ax, 29, 70, '5 racines permutées', 'varie', 's')
for i in range(5):
    disc(ax, 12 + i * 9.5, 57, 3.2, 'sujet')
disc(ax, 70, 57, 3.2, 'fixe')
text(ax, 70, 48, '6e racine fixée', 'fixe', 's')
box(ax, 6, 26, 72, 8, 'autre', label=r'$S_6$ : 720 permutations')
box(ax, 6, 10, 12, 8, 'sujet', label=r'$S_5$')
text(ax, 21, 14, '120 permutations', 'sujet', 's', ha='left')
text(ax, 52, 14, r'$\neq S_6$ : trop petit', 'limite', 's', ha='left')
save(fig, '67-213')
