import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(80)
box(ax, 4, 62, 36, 12, 'sujet', label=r'$x^2-2$ (de $\sqrt{2}$)', size='s')
text(ax, 44, 68, r'$\times$', 'encre', 'l')
box(ax, 48, 62, 36, 12, 'autre', label=r'$x^2-3$ (de $\sqrt{3}$)', size='s')
box(ax, 3, 14, 82, 36, 'resultat', fill=False, dash=True)
text(ax, 8, 45, r'$E$', 'resultat', 'm')
f = numberline(ax, 10, 78, 30, -2, 2, step=1, labels=False, arrow_right=False)
for v, role, up, l in [(-math.sqrt(2), 'sujet', True, r'$-\sqrt{2}$'), (math.sqrt(2), 'sujet', True, r'$\sqrt{2}$'),
                       (-math.sqrt(3), 'autre', False, r'$-\sqrt{3}$'), (math.sqrt(3), 'autre', False, r'$\sqrt{3}$')]:
    disc(ax, f(v), 30, 2, role)
    text(ax, f(v), 37 if up else 23, l, role, 's')
text(ax, 44, 6, 'les 4 racines sont dans $E$', 'resultat', 's')
save(fig, '63-109')
