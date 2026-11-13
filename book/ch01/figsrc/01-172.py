import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(70)
ys = np.array([60, 54, 47, 40, 34.]); xl = np.array([14, 11, 10, 11, 14.])
p = np.polyfit(ys, xl, 4); yy = np.linspace(34, 60, 40); xx = np.polyval(p, yy)
line(ax, list(zip(xx, yy)), 'sujet', lw=1.4)
line(ax, list(zip(38 - xx, yy)), 'sujet', lw=1.4)
text(ax, 19, 53, '4', 'sujet', 'l', weight='bold')
line(ax, [(22, 53), (31, 55)], 'fixe', lw=0.6)
text(ax, 32, 55, r'$n$ = 4 : numéro de ligne', 'sujet', 's', ha='left')
text(ax, 19, 41, '2', 'varie', 'l', weight='bold')
line(ax, [(22, 41), (31, 39)], 'fixe', lw=0.6)
text(ax, 32, 39, r'$k$ = 2 : position (dès 0)', 'varie', 's', ha='left')
for i, (x, s) in enumerate(zip([19, 31, 43, 55, 67], '14641')):
    if i == 2:
        box(ax, x, 14, 10, 8, 'resultat', label=s, weight='bold')
    else:
        box(ax, x, 14, 10, 8, 'fixe', label=s)
for i, x in enumerate([24, 36, 48, 60, 72]):
    if i == 2: text(ax, x, 8, '2', 'varie', 's', weight='bold')
    else: text(ax, x, 8, str(i), 'fixe', 's')
arrow(ax, (19, 32), (48, 22.5), 'resultat', curve=-0.3)
save(fig, '01-172')
