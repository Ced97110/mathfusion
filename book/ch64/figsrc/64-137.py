import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
h, gap = 9, 8
widths = [34, 38, 42, 60, 76]
labels = [r'$(12)(34)$ dans $N$', r'$(13)(24)$ dans $N$', r'$(135)$ dans $N$',
          r'tous les 3-cycles dans $N$', r'$N=A_5$ : 60 éléments']
steps = ['cas 5', 'cas 5', 'lemme B', 'lemme A']
ys = [2 + (h + gap) * (4 - k) for k in range(5)]   # de haut en bas
cx = 44
for k in range(5):
    role = 'resultat' if k == 4 else 'sujet'
    box(ax, cx - widths[k] / 2, ys[k], widths[k], h, role, label=labels[k])
for k in range(4):
    arrow(ax, (cx, ys[k] - 0.3), (cx, ys[k + 1] + h + 0.3), 'varie')
    text(ax, cx + 4, ys[k] - gap / 2, steps[k], 'varie', 's', ha='left')
save(fig, '64-137')
