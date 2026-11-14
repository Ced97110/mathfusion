import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 13, 68, 'un corps à 4', 'sujet', 's')
text(ax, 75, 68, 'un autre à 4', 'autre', 's')
text(ax, 44, 62, 'bijection', 'varie', 's')
L = ['0', '1', r'$\alpha$', r'$\alpha+1$']
R = ['0', '1', r'$\beta$', r'$\beta+1$']
for k in range(4):
    y = 46 - k * 13
    box(ax, 3, y, 20, 9, 'sujet', label=L[k])
    box(ax, 65, y, 20, 9, 'autre', label=R[k])
    arrow(ax, (24, y + 4.5), (64, y + 4.5), 'varie')
text(ax, 44, 4, 'seuls les noms changent', 'fixe', 's')
save(fig, '67-066')
