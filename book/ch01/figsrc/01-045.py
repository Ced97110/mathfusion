import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 22, 86, 'Descendre', 'varie', 'm', weight='bold')
text(ax, 68, 86, 'Remonter', 'resultat', 'm', weight='bold')
L = ['3 + 2 = (2 + 2)⁺', '2 + 2 = (1 + 2)⁺', '1 + 2 = (0 + 2)⁺']
for l, y in zip(L, (76, 60, 44)):
    box(ax, 5, y - 4, 34, 8, 'varie', label=l, size='m')
R = ['1 + 2 = 3', '2 + 2 = 4', '3 + 2 = 5']
for i, (r, y) in enumerate(zip(R, (44, 60, 76))):
    box(ax, 51, y - 4, 34, 8, 'resultat', label=r, size='m', weight='bold' if i == 2 else 'normal', lw=1.4 if i == 2 else 0.8)
box(ax, 30, 20, 28, 8, 'sujet', label='0 + 2 = 2', size='m', weight='bold')
arrow(ax, (22, 72), (22, 64), 'varie'); text(ax, 31, 68, '3 = 2⁺', 'varie', 's')
arrow(ax, (22, 56), (22, 48), 'varie'); text(ax, 31, 52, '2 = 1⁺', 'varie', 's')
arrow(ax, (22, 40), (34, 28), 'varie'); text(ax, 21, 33, '1 = 0⁺', 'varie', 's')
arrow(ax, (54, 28), (66, 40), 'resultat')
arrow(ax, (68, 48), (68, 56), 'resultat')
arrow(ax, (68, 64), (68, 72), 'resultat')
text(ax, 78, 52, 'suivant', 'resultat', 's')
text(ax, 44, 10, '3 étapes, 3 suivants', 'fixe', 's')
save(fig, '01-045')
