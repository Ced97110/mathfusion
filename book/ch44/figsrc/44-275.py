import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'$GL_2(\mathbb{R})$ : matrice du quart de tour', 'sujet', 'm', weight='bold')
c = 14.0; X, Y = 8.0, 28.0
vals = [['0', '-1'], ['1', '0']]; lets = [['a', 'b'], ['c', 'd']]
for r in range(2):
    for k in range(2):
        role = 'sujet' if r == k else 'varie'
        box(ax, X + k * c, Y + (1 - r) * c, c, c, role, label=vals[r][k].replace('-', '−'), size='l')
        text(ax, X + k * c + 2.5, Y + (1 - r) * c + c - 2.5, lets[r][k], role, 's')
text(ax, 56, 54, r'$ad = 0 \times 0 = 0$', 'sujet', 'm')
text(ax, 56, 44, r'$bc = (-1) \times 1 = -1$', 'varie', 'm')
text(ax, 56, 32, r'$ad - bc = 1 \neq 0$', 'resultat', 'm', weight='bold')
arrow(ax, (44, 26), (44, 17), 'fixe', lw=1.4)
box(ax, 8, 3, 72, 12, 'fixe', dash=True, label='même idée pour plus de lignes ?', size='s')
save(fig, '44-275')
