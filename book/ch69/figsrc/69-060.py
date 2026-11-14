import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(52)
f = numberline(ax, 8, 80, 22, -6, 6, labels=False, arrow_right=False)
for v in (-5, 0, 5):
    text(ax, f(v), 22 - 3.4, str(v), 'fixe', 's')
line(ax, [(f(-5), 30), (f(5), 30)], 'sujet', lw=3.0)
for v in (-5, 5):
    disc(ax, f(v), 30, 2.0, 'sujet', fill=False)
    line(ax, [(f(v), 23), (f(v), 28)], 'sujet', lw=0.5, dash=True)
for r in np.roots([1, 0, -3, 1]):
    disc(ax, f(r.real), 22, 1.6, 'resultat')
text(ax, f(-5), 37, r'$-\mu=-5$', 'sujet', 's')
text(ax, f(5), 37, r'$\mu=5$', 'sujet', 's')
text(ax, f(0), 40, 'toutes les racines', 'resultat', 's')
text(ax, f(0), 34, r'$(-\mu,\,\mu)$', 'sujet', 's')
save(fig, '69-060')
