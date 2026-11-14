import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(38)
f = numberline(ax, 6, 80, 12, 0, 30, 1, labels=False, arrow_right=False)
for v in (12, 19, 27):
    disc(ax, f(v), 12, 1.6, 'sujet'); text(ax, f(v), 5.5, str(v), 'sujet', 's')
arrow(ax, (f(12), 15), (f(19), 15), 'varie', curve=-0.45)
arrow(ax, (f(19), 15), (f(27), 15), 'varie', curve=-0.45)
text(ax, f(19) - 1, 24, '19 − 12 = 7', 'varie', 's', ha='right')
text(ax, f(19) + 1, 24, '27 − 19 = 8', 'varie', 's', ha='left')
text(ax, 44, 34, 'totaux voisins : on soustrait', 'encre', 's')
save(fig, '80-276')
