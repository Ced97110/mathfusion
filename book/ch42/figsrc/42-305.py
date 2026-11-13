import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 3, 12, 30, 50, 'fixe'); box(ax, 55, 12, 30, 50, 'fixe')
text(ax, 18, 67, 'départ', 'fixe', 'm'); text(ax, 70, 67, 'arrivée', 'fixe', 'm')
ys = [50, 38, 26, 18 + 0]
ys = [52 - 12 * i for i in range(4)]
lroles = ['sujet', 'sujet', 'fixe', 'fixe']
rroles = ['sujet', 'autre', 'autre', 'fixe']
rlab = [r'$e$', r'$y_1$', r'$y_2$', r'$y_3$']
for i, y in enumerate(ys):
    disc(ax, 18, y, 3.2, lroles[i], label=r'$x_%d$' % (i + 1), size='s')
    disc(ax, 70, y, 3.2, 'autre' if i in (1, 2) else ('sujet' if i == 0 else 'fixe'), label=rlab[i], size='s')
targets = [0, 0, 1, 2]
for i, t in enumerate(targets):
    arrow(ax, (21.4, ys[i]), (66.6, ys[t]), 'sujet' if i < 2 else 'autre')
text(ax, 18, 6, r'ker : ceux qui vont en $e$', 'sujet', 's')
text(ax, 70, 6, 'im : tous les atteints', 'autre', 's')
save(fig, '42-305')
