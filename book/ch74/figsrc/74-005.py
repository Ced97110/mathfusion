import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cols = [2, 32, 62]; w = 24
# frise
box(ax, cols[0], 32, w, 9, 'sujet')
for i in range(4): disc(ax, cols[0] + 3.6 + i * 5.6, 36.5, 2.0, 'sujet')
arrow(ax, (cols[0] + 2, 27), (cols[0] + w - 2, 27), 'varie')
text(ax, cols[0] + w / 2, 47, 'frise', 'sujet', 'l'); text(ax, cols[0] + w / 2, 22, '1 direction', 'varie', 's')
# papier peint
box(ax, cols[1], 20, w, w, 'autre')
for a in range(3):
    for b in range(3): disc(ax, cols[1] + 5 + a * 8, 25 + b * 8, 2.0, 'autre')
arrow(ax, (cols[1] + 2, 16), (cols[1] + w - 2, 16), 'varie'); arrow(ax, (cols[1] + w + 3, 44), (cols[1] + w + 3, 22), 'varie')
text(ax, cols[1] + w / 2, 52, 'papier peint', 'autre', 'm'); text(ax, cols[1] + w / 2, 10, '2 directions', 'varie', 's')
# tableau
box(ax, cols[2], 20, w, w, 'fixe')
disc(ax, cols[2] + w / 2, 33, 4.5, 'fixe')
text(ax, cols[2] + w / 2, 52, 'tableau', 'fixe', 'l'); text(ax, cols[2] + w / 2, 10, '0 direction', 'fixe', 's')
save(fig, '74-005')
