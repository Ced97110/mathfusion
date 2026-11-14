import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 2, 46, r'premiers avec 16 : $\varphi$(16) = 8', 'resultat', 'm', ha='left')
for i, k in enumerate(range(1, 16, 2)):
    box(ax, 8 + i * 9, 31, 8, 8, 'sujet' if k == 9 else 'resultat', label=str(k), size='s', r=0.6)
text(ax, 2, 22, 'multiples de 9 : 16 pas, 16 cases', 'varie', 'm', ha='left')
vis = {0: '9', 1: '2', 2: '11'}
for i in range(16):
    box(ax, 4 + i * 5, 8, 4.4, 5, 'sujet' if i == 0 else 'varie', label=vis.get(i), size='s', r=0.5)
for i in range(2):
    arrow(ax, (6.2 + i * 5, 14), (11.2 + i * 5, 14), 'varie', curve=-0.6, lw=0.8)
save(fig, '46-135')
