import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
y = 26
f = numberline(ax, 8, 78, y, -3, 3, labels=False, arrow_right=False)
line(ax, [(f(-3), y), (f(0) - 3, y)], 'autre', lw=3)
line(ax, [(f(0) + 3, y), (f(3), y)], 'resultat', lw=3)
disc(ax, f(0), y, 2, 'fixe')
brace(ax, f(-3), f(0) - 3, 20, 'autre', label='N')
brace(ax, f(0) + 3, f(3), 20, 'resultat', label='P')
text(ax, f(0), 16.3, '{0}', 'fixe', 's')
text(ax, 44, 40, 'F = P ∪ {0} ∪ N', 'sujet', 'l')
text(ax, 44, 33, 'trois morceaux, sans recouvrement', 'fixe', 's')
save(fig, '69-023')
