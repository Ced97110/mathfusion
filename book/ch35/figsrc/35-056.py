import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
f = numberline(ax, 14, 74, 30, -1, 1, step=0.5, arrow_right=False, size='s')
line(ax, [(f(0.866), 12), (f(0.866), 56)], 'resultat', lw=1.0, dash=True)
text(ax, f(0.866), 59, '2 sin 60° sin 30° = 0,866', 'resultat', 's')
arrow(ax, (f(0), 38), (f(0.866), 38), 'resultat', lw=1.3)
text(ax, 44, 46, 'cos 30° − cos 90°', 'sujet', 's')
text(ax, 44, 42, 'en premier : +0,866', 'resultat', 's')
arrow(ax, (f(0), 22), (f(-0.866), 22), 'limite', lw=1.3)
text(ax, 44, 17, 'cos 90° − cos 30°', 'autre', 's')
text(ax, 44, 13, 'ordre inversé : −0,866', 'limite', 's')
save(fig, '35-056')
