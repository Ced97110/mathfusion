import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 2, 12, 38, 42, 'sujet', fill=False, dash=True); text(ax, 21, 59, r'$S$ : des pions', 'sujet', 'm')
import itertools
pts = [(9 + 9 * c, 20 + 9 * r) for r in range(4) for c in range(3)]
for p in pts: disc(ax, p[0] + 3, p[1] + 3, 1.7, 'sujet')
text(ax, 21, 7, r'$x\in S$', 'sujet', 'm')
box(ax, 48, 12, 38, 42, 'autre', fill=False, dash=True); text(ax, 67, 59, r'$S/E$ : des boîtes', 'autre', 'm')
for i, (n, lab) in enumerate([(4, 'A'), (5, 'B'), (3, 'C')]):
    yy = 40.6 - i * 13.3
    box(ax, 51, yy, 32, 11, 'autre', label=None)
    text(ax, 55, yy + 5.5, lab, 'autre', 'm')
    for k in range(n): disc(ax, 63 + k * 4.2, yy + 5.5, 1.3, 'autre')
text(ax, 67, 7, r'$A\in S/E$ et $A\notin S$', 'autre', 's')
save(fig, '43-077')
