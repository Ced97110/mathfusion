import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
f = numberline(ax, 10, 78, 40, 28, 32, 1, arrow_right=False, size='s')
for v, r in ((29, 'autre'), (31, 'varie')): disc(ax, f(v), 40, 1.5, r)
disc(ax, f(30), 40, 1.8, 'sujet')
arrow(ax, (f(30) - 2, 43), (f(29) + 1, 43), 'autre', curve=-0.4) if False else None
arrow(ax, (f(30), 44), (f(29), 44), 'autre', curve=0.5); arrow(ax, (f(30), 44), (f(31), 44), 'varie', curve=-0.5)
text(ax, (f(29) + f(30)) / 2, 51, '1', 'autre', 's'); text(ax, (f(30) + f(31)) / 2, 51, '1', 'varie', 's')
text(ax, 44, 26, r'$31\times 29=(30+1)(30-1)$', 'encre', 'm')
text(ax, 44, 17, r'$=30^2-1^2=900-1$', 'encre', 'm')
text(ax, 44, 8, r'$=899$', 'resultat', 'l', weight='bold')
save(fig, '15-123')
