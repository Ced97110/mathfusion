import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 58, 'files de 3 élèves', 'sujet', 's')
text(ax, 66, 58, 'files paires de 5', 'autre', 's')
ys = [42, 26, 10]
left = ['6', '3', '1']; right = ['60', '60', '60']
mid = [r'$G$', r'$G^{\prime}$', r'$G^{\prime\prime}$']
for i, y in enumerate(ys):
    box(ax, 10, y, 24, 8, 'resultat' if i == 2 else 'sujet', label=left[i])
    box(ax, 54, y, 24, 8, 'limite' if i == 2 else 'autre', label=right[i])
    text(ax, 44, y + 4, mid[i], 'fixe', 'm')
    if i < 2:
        arrow(ax, (22, y), (22, ys[i + 1] + 8), 'varie')
        arrow(ax, (66, y), (66, ys[i + 1] + 8), 'varie')
text(ax, 22, 3, r'atteint $\{e\}$ : résoluble', 'resultat', 's')
text(ax, 66, 3, 'reste 60 : non résoluble', 'limite', 's')
save(fig, '64-067')
