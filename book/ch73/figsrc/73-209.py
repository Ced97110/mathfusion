import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
labels = [r'$\{1\}$', r'$G_1$', r'$G_2$', r'$G_3$', r'$G$']
x0, w, h, step = 10, 26, 9, 18
ys = [6 + step * i for i in range(5)]
for y, l in zip(ys, labels):
    box(ax, x0, y, w, h, 'sujet', label=l)
text(ax, 54, ys[-1] + h + 4, 'quotients', 'fixe', 's')
for i in range(4):
    role = 'varie' if i == 2 else 'fixe'
    arrow(ax, (x0 + w / 2, ys[i] + h), (x0 + w / 2, ys[i + 1]), role)
    yc = ys[i] + h + (step - h) / 2
    lab = 'simple, non commutatif' if i == 2 else 'commutatif'
    text(ax, x0 + w / 2 + 5, yc, lab, role, 'm', ha='left', weight='bold' if i == 2 else 'normal')
save(fig, '73-209')
