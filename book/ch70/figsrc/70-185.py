import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(84)
X = lambda x: 6 + x * 16
Y = lambda y: 48 + y * 12
p = lambda x: (x - 2) * (x - 1) * (x - 3)
line(ax, [(6, 48), (70, 48)], 'fixe', lw=0.6)
for xv in (1, 2, 3):
    line(ax, [(X(xv), 20), (X(xv), 80)], 'fixe', dash=True, lw=0.7)
    disc(ax, X(xv), 48, 1.3, 'varie'); text(ax, X(xv) + 2.4, 44.5, str(xv), 'varie', 's')
for lo, hi in ((1, 2), (3, 4)):
    t = np.linspace(lo, hi, 60)
    for sg in (1, -1):
        line(ax, [(X(a), Y(sg * np.sqrt(max(p(a), 0)))) for a in t], 'sujet', lw=1.6)
# cells above intervals 2 and 4 : outside, inside, outside separated by the two points
for xm in (1.5, 3.5):
    r = np.sqrt(p(xm))
    line(ax, [(X(xm), Y(r)), (X(xm), 80)], 'fixe', lw=2.2)
    line(ax, [(X(xm), Y(-r)), (X(xm), Y(r))], 'resultat', lw=2.2)
    line(ax, [(X(xm), 22), (X(xm), Y(-r))], 'fixe', lw=2.2)
    disc(ax, X(xm), Y(r), 1.2, 'sujet'); disc(ax, X(xm), Y(-r), 1.2, 'sujet')
for xm in (0.5, 2.5):
    line(ax, [(X(xm), 22), (X(xm), 80)], 'fixe', lw=2.2)
for (lo, hi), role, lab in (((0, 1), 'fixe', 'aucun point'), ((1, 2), 'resultat', '2 points'),
                            ((2, 3), 'fixe', 'aucun point'), ((3, 4), 'resultat', '2 points')):
    brace(ax, X(lo) + 1, X(hi) - 1, 18, role, label=lab)
text(ax, 79, 68, r'$y^2=p(x)$', 'sujet', 's')
save(fig, '70-185')
