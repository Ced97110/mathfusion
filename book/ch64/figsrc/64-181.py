import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'$p=4$ n’est pas premier', 'limite', 'm')
V = {1: (13, 52), 2: (35, 52), 3: (35, 30), 4: (13, 30)}
poly(ax, list(V.values()), 'fixe')
arrow(ax, (17, 49), (31, 33), 'varie', both=True)
for k, (x, y) in V.items():
    disc(ax, x, y, 2.6, 'sujet', label=str(k), size='s')
for a, b, c in ((1, 2, (24, 58)), (2, 3, (41, 41)), (3, 4, (24, 24)), (4, 1, (7, 41))):
    pass
arrow(ax, (17, 55.5), (31, 55.5), 'sujet'); arrow(ax, (38.5, 48), (38.5, 34), 'sujet')
arrow(ax, (31, 26.5), (17, 26.5), 'sujet'); arrow(ax, (9.5, 34), (9.5, 48), 'sujet')
text(ax, 24, 61, '(1 2 3 4)', 'sujet', 's'); text(ax, 18, 40, '(1 3)', 'varie', 's')
box(ax, 50, 42, 36, 14, 'sujet', label='engendrent 8 éléments', size='s')
box(ax, 50, 14, 36, 14, 'limite', label=r'$S_4$ : 24 non atteint', size='s')
arrow(ax, (68, 41), (68, 29), 'limite', lw=0.8)
text(ax, 71, 35, 'pas tout', 'limite', 's', ha='left')
save(fig, '64-181')
