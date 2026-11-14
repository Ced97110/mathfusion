import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 16, 75, r'$S$ : élèves', 'sujet', 's')
text(ax, 72, 75, r'$F$ : notes', 'autre', 's')
text(ax, 44, 68, 'une application', 'varie', 's')
ys = [56, 40, 24]
for y, n in zip(ys, ('Ana', 'Bob', 'Chi')):
    box(ax, 4, y, 24, 10, 'sujet', label=n)
for y, n in zip(ys, ('0', '1', '2')):
    box(ax, 60, y, 24, 10, 'autre', label=n)
for y0, y1 in ((56, 24), (40, 56), (24, 40)):
    arrow(ax, (28, y0 + 5), (60, y1 + 5), 'varie')
box(ax, 4, 2, 80, 14, 'resultat', label=r'$F^S$ : 27 applications' + '\n' + r'$3\times3\times3$', size='s')
save(fig, '55-018')
