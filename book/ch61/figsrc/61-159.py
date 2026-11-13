import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
ys = [4, 22, 40, 58]
labs = [r'$F_0=\mathbb{Q}$', r'$F_1$', r'$F_2$', r'$F_3$']
for i, (y, l) in enumerate(zip(ys, labs)):
    box(ax, 6, y, 30, 10, 'fixe' if i == 0 else 'sujet', label=l)
for i, d in enumerate(['2', '1', '2']):
    arrow(ax, (21, ys[i] + 10), (21, ys[i + 1]), 'varie')
    text(ax, 25, ys[i] + 14, 'degré ' + d, 'varie', 's', ha='left')
box(ax, 46, 56, 38, 12, 'varie', label=r'$2\times1\times2$')
arrow(ax, (65, 56), (65, 48), 'varie')
box(ax, 46, 36, 38, 12, 'resultat', label=r'$=4=2^{2}$')
arrow(ax, (65, 36), (65, 28), 'varie')
box(ax, 46, 14, 38, 14, 'autre', label=r'$z$ : degré 1, 2 ou 4', size='s')
text(ax, 65, 9, 'divise 4', 'autre', 's')
save(fig, '61-159')
