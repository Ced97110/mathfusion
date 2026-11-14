import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(80)
text(ax, 44, 74, r'$x^2-2$ est irréductible', 'encre', 'm')
f = numberline(ax, 14, 74, 40, -2, 2, step=1, labels=False, arrow_right=False)
for v, l in [(-math.sqrt(2), r'$-\sqrt{2}$'), (math.sqrt(2), r'$\sqrt{2}$')]:
    disc(ax, f(v), 40, 2.2, 'resultat')
    text(ax, f(v), 32, l, 'resultat', 's')
box(ax, 4, 54, 36, 14, 'sujet', label='Jacobson :\nracines distinctes', size='s')
box(ax, 48, 54, 36, 14, 'autre', label='Judson :\nracines distinctes', size='s')
arrow(ax, (22, 54), (f(-math.sqrt(2)) + 1.5, 43), 'sujet')
arrow(ax, (66, 54), (f(math.sqrt(2)) - 1.5, 43), 'autre')
text(ax, 44, 22, 'deux racines distinctes', 'resultat', 'm')
text(ax, 44, 14, 'dans les deux définitions', 'resultat', 's')
save(fig, '63-113')
