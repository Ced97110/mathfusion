import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
f = numberline(ax, 8, 70, 18, 0, 6)
disc(ax, f(2), 18, 2.2, 'sujet'); disc(ax, f(5), 18, 2.2, 'autre')
text(ax, f(2), 28, '2', 'sujet', 'xl'); text(ax, f(5), 28, '5', 'autre', 'xl')
arrow(ax, (f(2), 25), (f(2), 21), 'sujet'); arrow(ax, (f(5), 25), (f(5), 21), 'autre')
text(ax, 44, 41, 'couple (2, 5) ?', 'encre', 'l')
text(ax, 44, 5, 'deux points séparés, pas un', 'limite', 's')
save(fig, '19-011')
