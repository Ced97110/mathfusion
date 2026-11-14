import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
f = numberline(ax, 4, 76, 36, 0, 28, step=1, labels=False, arrow_right=True, tick=0.8)
text(ax, 4, 64, 'puissances de 2', 'sujet', 'm', ha='left')
for v in (2, 4, 8, 16):
    disc(ax, f(v), 36, 1.0, 'sujet'); text(ax, f(v), 44, str(v), 'sujet', 's')
text(ax, 4, 19, 'puissances de 3', 'autre', 'm', ha='left')
for v in (3, 9, 27):
    disc(ax, f(v), 36, 1.0, 'autre'); text(ax, f(v), 28, str(v), 'autre', 's')
disc(ax, f(6), 36, 1.2, 'limite'); text(ax, f(6), 44, '6', 'limite', 's')
arrow(ax, (f(6) + 1, 49), (f(6) + 1, 45.5), 'limite')
text(ax, 44, 55, r'$6=2\times3$ : dans aucune liste', 'limite', 's')
save(fig, '67-030')
