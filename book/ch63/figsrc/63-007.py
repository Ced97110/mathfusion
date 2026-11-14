import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 60, r'groupe $\{1,\sigma\}$', 'sujet', 'm')
text(ax, 68, 60, 'sous-groupe ↔ corps fixe', 'autre', 's')
text(ax, 7, 47, r'$\circ$', 'fixe', 'm')
for j, h in enumerate(['1', r'$\sigma$']):
    text(ax, 17 + 10 * j, 47, h, 'fixe', 'm')
rows = ['1', r'$\sigma$']
res = [['1', r'$\sigma$'], [r'$\sigma$', '1']]
for i in range(2):
    text(ax, 7, 37 - 10 * i, rows[i], 'fixe', 'm')
    for j in range(2):
        box(ax, 12 + 10 * j, 32 - 10 * i, 10, 10, 'resultat', label=res[i][j])
box(ax, 50, 36, 36, 12, 'sujet', label=r'$\{1\}\ \leftrightarrow\ \mathbb{Q}(\sqrt{2})$')
box(ax, 50, 18, 36, 12, 'sujet', label=r'$\{1,\sigma\}\ \leftrightarrow\ \mathbb{Q}$')
save(fig, '63-007')
