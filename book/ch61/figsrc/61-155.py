import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
labs = [('fixe', 'ℚ'), ('sujet', 'ℚ(√2)'), ('autre', 'ℚ(√2, √3)')]
ys = [6, 24, 42]
for (role, s), y in zip(labs, ys):
    box(ax, 24, y, 40, 11, role, label=s, size='m')
for i, rt in enumerate(['+ √2', '+ √3']):
    arrow(ax, (44, ys[i] + 11), (44, ys[i + 1]), 'varie')
    text(ax, 47, ys[i] + 14.5, rt, 'varie', 's', ha='left')
    text(ax, 41, ys[i] + 14.5, 'degré 2', 'varie', 's', ha='right')
save(fig, '61-155')
