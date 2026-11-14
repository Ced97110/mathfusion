import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
lx = [9, 26, 43, 60, 77]; dx = [14, 44, 74]
text(ax, 2, 78, r'$S$ : 5 lettres', 'sujet', 's', ha='left')
for i, x in enumerate(lx): box(ax, x - 5, 62, 10, 9, 'sujet', label=str(i + 1))
for k, x in enumerate(dx): box(ax, x - 12, 18, 24, 12, 'autre')
tgt = [0, 1, 2, 2, 2]
for i, x in enumerate(lx):
    t = tgt[i]
    off = (0, 0, -6, 0, 6)[i] if t == 2 else 0
    arrow(ax, (x, 62), (dx[t] + off, 30.5), 'varie' if i < 3 else 'limite')
text(ax, 2, 8, r'$T$ : 3 tiroirs', 'autre', 's', ha='left')
text(ax, 86, 8, 'deux lettres, un seul tiroir', 'limite', 's', ha='right')
save(fig, '43-111')
